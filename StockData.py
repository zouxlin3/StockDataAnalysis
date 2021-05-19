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
            else:
                self.dataframes[i] = pd.DataFrame(columns=('', 'OBJECT_ID', 'S_INFO_WINDCODE', 'TRADE_DT', 'CRNCY_CODE',
                                                  'S_DQ_PRECLOSE', 'S_DQ_OPEN', 'S_DQ_HIGH', 'S_DQ_LOW', 'S_DQ_CLOSE',
                                                  'S_DQ_CHANGE', 'S_DQ_PCTCHANGE', 'S_DQ_VOLUME', 'S_DQ_AMOUNT',
                                                  'S_DQ_ADJPRECLOSE', 'S_DQ_ADJOPEN', 'S_DQ_ADJHIGH', 'S_DQ_ADJLOW',
                                                  'S_DQ_ADJCLOSE', 'S_DQ_ADJFACTOR', 'S_DQ_AVGPRICE', 'S_DQ_TRADESTATUS'
                                                  , 'OPDATE', 'OPMODE'))  # 没有该股票csv时添加空dataframe

    def get_data_by_symbol(self, symbol: str, start_date: str, end_date: str):
        self.format_date(symbol)  # 按日期排序
        data = self.dataframes[symbol]
        data = data.sort_values(by='TRADE_DT')
        data = data.reset_index(drop=True)

        timedelta = pd.Timedelta(days=1)
        start_date = self.str2timestamp(start_date)
        end_date = self.str2timestamp(end_date)

        while len(data[(data['TRADE_DT'] == start_date)].index) == 0:  # 起始日期没有数据时，向后延
            start_date = start_date + timedelta
        while len(data[(data['TRADE_DT'] == end_date)].index) == 0:  # 终止日期没有数据时，向前延
            end_date = end_date - timedelta

        start_index = data[(data['TRADE_DT'] == start_date)].index[0]  # index返回int64index类型，取[0]即为int
        end_index = data[(data['TRADE_DT'] == end_date)].index[0]

        output = data.iloc[start_index:end_index+1]
        output = output.loc(axis=1)['TRADE_DT', 'S_DQ_OPEN', 'S_DQ_HIGH', 'S_DQ_LOW', 'S_DQ_CLOSE']
        output.columns = ['date', 'open', 'high', 'low', 'close']

        return output

    def get_data_by_date(self, adate: str, symbols: List[str]):
        output = pd.DataFrame(columns=('symbols', 'open', 'high', 'low', 'close'))
        adate = self.str2timestamp(adate)

        for i in symbols:
            self.format_date(i)
            data = self.dataframes[i]

            date_index = data[(data['TRADE_DT'] == adate)].index
            if len(date_index) == 0:  # 该日期没有数据时
                continue

            astock = data.iloc[date_index[0]]  # 取该股票日频数据中的一行
            astock = astock.loc(axis=0)['S_INFO_WINDCODE', 'S_DQ_OPEN', 'S_DQ_HIGH', 'S_DQ_LOW', 'S_DQ_CLOSE']
            astock.index = ['symbols', 'open', 'high', 'low', 'close']
            output = output.append(astock)  # 不能直接output.append

        output['symbols'] = output['symbols'].apply(lambda x: x[:6])  # 取S_INFO_WINDCODE的前6位，即股票代码
        return output

    def format_date(self, symbol: str):
        self.read([symbol])
        self.dataframes[symbol]['TRADE_DT'] = self.dataframes[symbol]['TRADE_DT'].apply(self.str2timestamp)

    def get_filepath(self, stock: str):  # 判断该股票csv是否存在
        filepath = self.filenames.get(stock)
        if filepath:
            return filepath
        else:
            return False

    def str2timestamp(self, date: str):
        date = int(date)
        year = date//10000
        month = (date % 10000)//100
        day = date % 100
        return pd.Timestamp(year, month, day)
