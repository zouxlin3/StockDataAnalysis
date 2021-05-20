from typing import List
import os
import pandas as pd
import matplotlib.pyplot as plt


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
            filepath = self.____get_filepath(i)
            if filepath:
                self.dataframes[i] = pd.read_csv(filepath)
                self.format_date(i)
            else:
                self.dataframes[i] = pd.DataFrame(columns=('', 'OBJECT_ID', 'S_INFO_WINDCODE', 'TRADE_DT', 'CRNCY_CODE',
                                                  'S_DQ_PRECLOSE', 'S_DQ_OPEN', 'S_DQ_HIGH', 'S_DQ_LOW', 'S_DQ_CLOSE',
                                                  'S_DQ_CHANGE', 'S_DQ_PCTCHANGE', 'S_DQ_VOLUME', 'S_DQ_AMOUNT',
                                                  'S_DQ_ADJPRECLOSE', 'S_DQ_ADJOPEN', 'S_DQ_ADJHIGH', 'S_DQ_ADJLOW',
                                                  'S_DQ_ADJCLOSE', 'S_DQ_ADJFACTOR', 'S_DQ_AVGPRICE', 'S_DQ_TRADESTATUS'
                                                  , 'OPDATE', 'OPMODE'))  # 没有该股票csv时添加空dataframe

    def get_data_by_symbol(self, symbol: str, start_date: str, end_date: str):
        data = self.dataframes[symbol]
        data = data.sort_values(by='TRADE_DT')  # 按日期排序
        data = data.reset_index(drop=True)

        timedelta = pd.Timedelta(days=1)
        start_date = self.____str2timestamp(start_date)
        end_date = self.____str2timestamp(end_date)

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
        adate = self.____str2timestamp(adate)

        for i in symbols:
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

    def get_data_by_field(self, field: str, symbols: List[str]):
        output = pd.DataFrame(columns=['date']+symbols)

        for i in symbols:
            data = self.dataframes[i]
            afield = data.loc(axis=1)['TRADE_DT', field]  # 读取股票i的date和field列数据
            afield.columns = ['date', i]

            for j in range(afield.shape[0]):
                date_index = output[(output['date'] == afield['date'][j])].index
                if len(date_index) == 0:  # 判断output中date列有无该时间戳，没有的话添加新的一行
                    output = output.append(afield.iloc[j])
                else:
                    output.loc[date_index, i] = afield.loc[j, i]

        output = output.sort_values(by='date')
        output = output.reset_index(drop=True)
        return output

    def plot(self, symbol: str, field: str):
        data = self.dataframes[symbol]
        data = data.sort_values(by='TRADE_DT')  # 根据时间排序
        data = data.reset_index(drop=True)

        changed_field = self.____field_change(field)
        data[changed_field] = data[changed_field].apply(self.____int_remove_nan)  # y轴及直方图数据
        y = data[changed_field].values.tolist()
        plt.ylabel(field)

        labels = data['TRADE_DT']  # x轴
        x = range(labels.shape[0])
        plt.xlabel('date')
        # plt.xticks(x, labels)

        plt.title(symbol)

        if field == 'volume' or field == 'turnover':
            plt.bar(x, y, width=0.35, linewidth=0.8, facecolor='tomato', edgecolor='orangered')
        else:
            plt.plot(x, y, c='tomato', linewidth=0.8)

        plt.savefig(os.path.join('figures', 'E2.2.jpg'), dpi=200)

    def format_date(self, symbol: str):
        self.dataframes[symbol]['TRADE_DT'] = self.dataframes[symbol]['TRADE_DT'].apply(self.____str2timestamp)

    def adjust_data(self, symbol: str):
        data = self.dataframes[symbol]
        data = data.sort_values(by='TRADE_DT')  # 根据时间排序
        data = data.reset_index(drop=True)

        rows = data.shape[0]
        data.loc[rows-1, 'forward_af'] = 1.0  # 计算前复权因子
        for i in range(rows-1):
            data.loc[rows-2-i, 'forward_af'] = self.____get_forward_af(data.loc[rows - 2 - i, 'S_DQ_CLOSE'],
                                                                       data.loc[rows-1-i, 'S_DQ_PRECLOSE'],
                                                                       data.loc[rows-1-i, 'forward_af'])

        for i in ['open', 'high', 'low', 'close']:  # 对代表价格计算复权价
            for j in range(rows-1):
                data.loc[rows-2-j, 'forward_adjust_'+i] = self.____forward_adjust_price(data.loc[rows - 2 - j, self.____field_change(i)],
                                                                                        data.loc[rows-2-j, 'forward_af'],
                                                                                        data.loc[rows-1-j, 'forward_af'])

        self.dataframes[symbol] = data

    def resample(self, symbol: str, freq: int):
        data = self.dataframes[symbol]
        data = data.sort_values(by='TRADE_DT')
        data = data.reset_index(drop=True)
        output = pd.DataFrame(columns=('date', 'open', 'close', 'high', 'low', 'volume', 'turnover', 'vwap'))

        rows = data.shape[0]
        for i in range(rows):
            if (i+1) % freq == 0:
                clip = data[i+1-freq:i+1]
                clip = clip.reset_index(drop=True)
                aresample = pd.Series({
                    'date': clip.loc[0, 'TRADE_DT'],
                    'open': clip.loc[0, 'S_DQ_OPEN'],
                    'close': clip.loc[freq-1, 'S_DQ_CLOSE'],
                    'high': max(clip.loc(axis=1)['S_DQ_HIGH'].values.tolist()),
                    'low': min(clip.loc(axis=1)['S_DQ_LOW'].values.tolist()),
                    'volume': sum(clip.loc(axis=1)['S_DQ_VOLUME'].values.tolist()),
                    'turnover': sum(clip.loc(axis=1)['S_DQ_AMOUNT'].values.tolist()),
                })
                if aresample['volume'] != 0:
                    aresample['vwap'] = round(aresample['turnover']/aresample['volume'], 4)  # 保留4位小数
                output = output.append(aresample, ignore_index=True)

        return output

    def ____get_filepath(self, stock: str):  # 判断该股票csv是否存在，返回csv路径
        filepath = self.filenames.get(stock)
        if filepath:
            return filepath
        else:
            return False

    def ____str2timestamp(self, date: str):
        date = int(date)
        year = date//10000
        month = (date % 10000)//100
        day = date % 100
        return pd.Timestamp(year, month, day)

    def ____field_change(self, field):
        fields = {
            'open': 'S_DQ_OPEN',
            'high': 'S_DQ_HIGH',
            'low': 'S_DQ_LOW',
            'close': 'S_DQ_CLOSE',
            'vwap': 'S_DQ_VWAP',
            'volume': 'S_DQ_VOLUME',
            'turnover': 'S_DQ_AMOUNT'
        }

        return fields[field]

    def ____int_remove_nan(self, value: str):  # str2int, 将NaN设为0
        if value != value:
            return 0
        else:
            return int(value)

    # close：当天收盘价  preclose：明天前收  foraf：明天复权因子
    def ____get_forward_af(self, close: str, preclose: str, foraf: float):
        return round((int(preclose)/int(close))*foraf, 5)  # 最多5位小数

    # price：当天价格
    def ____forward_adjust_price(self, price: str, today_af: float, torm_af: float):
        return int(price)*today_af/torm_af
