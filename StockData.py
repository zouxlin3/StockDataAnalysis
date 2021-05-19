from typing import List
import os
import pandas as pd


class StockData:
    def __init__(self, path: str):
        self.path = os.path.normpath(path)

        self.filenames = {}

        def add_filename():  # 遍历文件夹将csv文件路径加入到filenames
            for filename in os.listdir(self.path):
                filepath = os.path.join(self.path, filename)
                if os.path.isfile(filepath):
                    self.filenames[filename[:6]] = filepath
                else:
                    add_filename(filepath)
        add_filename()

        self.dataframes = {}

    def read(self, symbols: List[str]):  # dict结构
        for i in symbols:
            filepath = self.get_filepath(i)
            if filepath:
                self.dataframes[i] = pd.read_csv(filepath)

    def get_data_by_symbol(self, symbol: str, start_date: int, end_date: int):
        filepath = self.get_filepath(symbol)
        if filepath:
            data = pd.read_csv(filepath)

        data['TRADE_DT'] = data['TRADE_DT'].apply(int)  # 按日期排序
        data = data.sort_values(by='TRADE_DT')
        data = data.reset_index(drop=True)

        while len(data[(data['TRADE_DT'] == start_date)].index) == 0:  # 起始日期没有数据时，向后延
            day = start_date % 100
            month = start_date % 1000
            if day == 31:
                if month > 1200:
                    start_date = (start_date/1000 + 1)*1000 + 101
                else:
                    start_date = (start_date/100 + 1)*100 + 1
            else:
                start_date = start_date + 1
        start_index = data[(data['TRADE_DT'] == start_date)].index[0]  # index返回int64index类型，取[0]即为int

        while len(data[(data['TRADE_DT'] == end_date)].index) == 0:  # 终止日期没有数据时，向前延
            day = end_date % 100
            month = end_date % 1000
            if day == 1:
                if month < 200:
                    end_date = (end_date/1000 - 1)*1000 + 1231
                else:
                    end_date = (end_date/100 - 1)*100 + 31
            else:
                end_date = end_date - 1
        end_index = data[(data['TRADE_DT'] == end_date)].index[0]

        output = data.iloc[start_index:end_index+1]
        output = output.loc(axis=1)['TRADE_DT', 'S_DQ_OPEN', 'S_DQ_HIGH', 'S_DQ_LOW', 'S_DQ_CLOSE']
        output.columns = ['date', 'open', 'high', 'low', 'close']

        return output

    def get_data_by_date(self, adate: str, symbols: List[str]):
        output = pd.DataFrame(columns=('symbols', 'open', 'high', 'low', 'close'))
        for i in symbols:
            filepath = self.get_filepath(i)
            if filepath:
                data = pd.read_csv(filepath)
            else:
                continue

    def get_filepath(self, stock: str):  # 判断该股票csv是否存在
        filepath = self.filenames.get(stock)
        if filepath:
            return filepath
        else:
            print('There is no stock: ' + stock)
            return False
