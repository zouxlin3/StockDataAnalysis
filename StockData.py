from typing import List
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calendar
from math import pow


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
            filepath = self.__get_filepath(i)
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

        timedelta = pd.Timedelta(days=1)
        start_date = self.__str2timestamp(start_date)
        end_date = self.__str2timestamp(end_date)

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
        adate = self.__str2timestamp(adate)

        for i in symbols:
            data = self.dataframes[i]

            date_index = data[(data['TRADE_DT'] == adate)].index
            if len(date_index) == 0:  # 该日期没有数据时
                output.append(pd.Series({'symbols': i}), ignore_index=True)
                continue

            astock = data.iloc[date_index[0]]  # 取该股票日频数据中的一行
            astock = astock.loc(axis=0)['S_INFO_WINDCODE', 'S_DQ_OPEN', 'S_DQ_HIGH', 'S_DQ_LOW', 'S_DQ_CLOSE']
            astock.index = ['symbols', 'open', 'high', 'low', 'close']
            output = output.append(astock)  # 不能直接output.append

        output['symbols'] = output['symbols'].apply(lambda x: x[:6])  # 取S_INFO_WINDCODE的前6位，即股票代码
        output = output.reset_index(drop=True)
        return output

    def get_data_by_field(self, field: str, symbols: List[str]):
        output = pd.DataFrame(columns=['date']+symbols)

        for i in symbols:
            data = self.dataframes[i]
            afield = data.loc(axis=1)['TRADE_DT', self.__field_change(field)]  # 读取股票i的date和field列数据
            afield.columns = ['date', i]

            for j in range(afield.shape[0]):  # 遍历afield所有行
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
        changed_field = self.__field_change(field)

        data[changed_field] = data[changed_field].apply(self.__int_remove_nan)  # y轴及直方图数据
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
        self.dataframes[symbol]['TRADE_DT'] = self.dataframes[symbol]['TRADE_DT'].apply(self.__str2timestamp)
        self.dataframes[symbol] = self.dataframes[symbol].sort_values(by='TRADE_DT')  # 根据时间排序
        self.dataframes[symbol] = self.dataframes[symbol].reset_index(drop=True)

    def adjust_data(self, symbol: str):
        data = self.dataframes[symbol]

        rows = data.shape[0]
        data.loc[rows-1, 'forward_af'] = 1.0  # 计算前复权因子
        for i in range(rows-1):
            data.loc[rows-2-i, 'forward_af'] = self.__get_forward_af(data.loc[rows - 2 - i, 'S_DQ_CLOSE'],
                                                                     data.loc[rows-1-i, 'S_DQ_PRECLOSE'],
                                                                     data.loc[rows-1-i, 'forward_af'])

        for i in ['open', 'high', 'low', 'close']:  # 对代表价格计算前复权价
            data.loc[rows-1, 'forward_adjust_'+i] = data.loc[rows-1, self.__field_change(i)]  # 最新日期的前复权价取原值
            for j in range(rows-1):
                data.loc[rows-2-j, 'forward_adjust_'+i] = self.__forward_adjust_price(data.loc[rows - 2 - j, self.__field_change(i)],
                                                                                      data.loc[rows-2-j, 'forward_af'],
                                                                                      data.loc[rows-1-j, 'forward_af'])

        self.dataframes[symbol] = data

    def resample(self, symbol: str, freq: int):
        data = self.dataframes[symbol]
        output = pd.DataFrame(columns=('date', 'open', 'close', 'high', 'low', 'volume', 'turnover', 'vwap'))

        rows = data.shape[0]
        for i in range(rows):  # 遍历data每一行
            if (i+1) % freq == 0:  # 行数达到freq倍数时进行一次重采样
                clip = data[i+1-freq:i+1]  # 选取前freq行
                clip = clip.reset_index(drop=True)
                aline = pd.Series({
                    'date': clip.loc[freq-1, 'TRADE_DT'],
                    'open': clip.loc[0, 'S_DQ_OPEN'],
                    'close': clip.loc[freq-1, 'S_DQ_CLOSE'],
                    'high': max(clip.loc(axis=1)['S_DQ_HIGH'].values.tolist()),
                    'low': min(clip.loc(axis=1)['S_DQ_LOW'].values.tolist()),
                    'volume': round(sum(clip.loc(axis=1)['S_DQ_VOLUME'].values.tolist()), 0),
                    'turnover': sum(clip.loc(axis=1)['S_DQ_AMOUNT'].values.tolist()),
                })
                if aline['volume'] != 0:
                    aline['vwap'] = round(aline['turnover']/aline['volume'], 4)  # 保留4位小数
                output = output.append(aline, ignore_index=True)

        return output

    def moving_average(self, symbol: str, field: str, window: int):  # 先使用adjust_data
        data = self.dataframes[symbol]

        output = data['forward_adjust_'+field].rolling(window).mean()
        output.index = data['TRADE_DT']
        return output

    '''
    EMA Calculation
    There are three steps to calculate the EMA. Here is the formula for a 5 Period EMA

    1. Calculate the SMA  # values为S_DQ_AVGPRICE
    (Period Values / Number of Periods)
    
    2. Calculate the Multiplier
    2 / (Number of Periods + 1)

    3. Calculate the EMA
    For the first EMA, we use the SMA(previous day) instead of EMA(previous day).
    EMA = {Close - EMA(previous day)} x multiplier + EMA(previous day)
    '''
    def ema(self, symbol: str, periods: int):  # 先使用adjust_data
        data = self.dataframes[symbol]

        data['sma_'+str(periods)] = data['S_DQ_AVGPRICE'].rolling(periods).mean()  # 计算sma
        multiplier = 2/(periods+1)

        data.loc[periods-1, 'ema_'+str(periods)] = data.loc[periods-1, 'sma_'+str(periods)]  # 将第一个ema设为同日的sma
        for i in range(data.shape[0]-periods):  # 从第二个ema开始计算
            data.loc[i+periods, 'ema_'+str(periods)] = (data.loc[i+periods, 'forward_adjust_close']-data.loc[i+periods-1, 'ema_'+str(periods)])\
                                         * multiplier+data.loc[i+periods-1, 'ema_'+str(periods)]

        output = data['ema_'+str(periods)]
        output.index = data['TRADE_DT']
        return output

    def atr(self, symbol: str, periods: int):  # 先使用adjust_data
        data = self.dataframes[symbol]

        for i in range(data.shape[0]):  # 遍历每一行，计算mtr
            data.loc[i, 'mtr'] = self.__calculate_mtr(data.loc[i, 'forward_adjust_high'], data.loc[i, 'forward_adjust_low'], data.loc[i, 'S_DQ_PRECLOSE'])

        data['atr_'+str(periods)] = data['mtr'].rolling(periods).mean()  # 过去periods天的mtr平均值
        output = data.loc(axis=1)['atr_'+str(periods)]
        output.index = data["TRADE_DT"]
        return output

    def rsi(self, symbol: str, periods: int):  # 先使用adjust_data
        data = self.dataframes[symbol]

        for i in range(data.shape[0]-periods):  # 从第periods行开始遍历每一行
            pctchanges = data.loc[i:i+periods, 'S_DQ_PCTCHANGE'].values.tolist()  # 将一个periosd内的pctchange放入列表
            data.loc[i+periods, 'rsi_'+str(periods)] = self.__calculate_rsi(pctchanges)  # 计算该periods内的rsi

        output = data['rsi_'+str(periods)]
        output.index = data['TRADE_DT']
        return output

    '''
    DIF＝EMA(short)-EMA(long)
    DEA为DIF移动平均
    MACD＝(DIF-DEA)*2
    '''
    def macd(self, symbol: str, long: int, short: int, dea_periods: int):  # 先使用adjust_data
        data = self.dataframes[symbol]

        self.ema(symbol, long)
        self.ema(symbol, short)

        for i in range(data.shape[0]):  # 计算dif
            data.loc[i, 'dif'] = data.loc[i, 'ema_'+str(short)] - data.loc[i, 'ema_'+str(long)]

        data['dea_'+str(dea_periods)] = data['dif'].rolling(dea_periods).mean()  # 计算dea

        for i in range(data.shape[0]):  # 计算macd
            data.loc[i, 'macd'] = (data.loc[i, 'dif'] - data.loc[i, 'dea_'+str(dea_periods)])

        output = data['macd']
        output.index = data['TRADE_DT']
        return output

    def calc_return(self, symbol: str, freq: str):  # 先使用adjust_data
        dates = self.__get_date_by_freq(symbol, freq)  # 该freq下所有时间段的起始终止时间
        data = self.dataframes[symbol]
        output = pd.DataFrame(columns=('date', 'return_'+freq))

        for i in range(dates.shape[0]):
            output = output.append(pd.Series({'date': dates.loc[i, 'end']}), ignore_index=True)

            start_index = data[(data['TRADE_DT'] == dates.loc[i, 'start'])].index[0]  # 用close计算return
            end_index = data[(data['TRADE_DT'] == dates.loc[i, 'end'])].index[0]
            start_close = data.loc[start_index, 'forward_adjust_close']
            end_close = data.loc[end_index, 'forward_adjust_close']
            ret = ((end_close - start_close)/start_close)*100  # 百分比

            output.loc[i, 'return'] = round(ret, 4)  # 保留4位小数
        return output

    def calc_sharpe_ratio(self, symbol: str, freq: str):  # 先使用adjust_data
        return_df = self.calc_return(symbol, freq)

        std = return_df.std(axis=0)['return']
        mean = return_df.mean(axis=0)['return']
        rfr_year = 0.03
        rfrs = {
            'm': pow(1+rfr_year, 1/12)-1,
            'q': pow(1+rfr_year, 1/4)-1,
            'h': pow(1+rfr_year, 1/2)-1,
            'y': rfr_year
        }  # 不同freq的无风险利率（%）

        return (mean-rfrs[freq]*100)/std  # 夏普比率=（收益率-无风险利率）/收益率方差

    def calc_max_drawdown_ratio(self, symbol: str):  # 先使用adjust_data
        data = self.dataframes[symbol]

        pre_max = 0
        max_drawdown_ratio = 0

        for i in range(data.shape[0]):  # 遍历data每一行
            close = data.loc[i, 'forward_adjust_close']
            if close > pre_max:  # 当日之前的最大值
                pre_max = close

            drawdown_ratio = (1-close/pre_max)*100  # 计算当日回撤率
            if drawdown_ratio > max_drawdown_ratio:  # 判断最大回撤率
                max_drawdown_ratio = drawdown_ratio

        return max_drawdown_ratio

    def __get_filepath(self, stock: str):  # 判断该股票csv是否存在，返回csv路径
        filepath = self.filenames.get(stock)
        if filepath:
            return filepath
        else:
            return False

    def __str2timestamp(self, date: str):
        date = int(date)
        year = date//10000
        month = (date % 10000)//100
        day = date % 100
        return pd.Timestamp(year, month, day)

    def __field_change(self, field):
        fields = {
            'open': 'S_DQ_OPEN',
            'high': 'S_DQ_HIGH',
            'low': 'S_DQ_LOW',
            'close': 'S_DQ_CLOSE',
            'vwap': 'S_DQ_VWAP',
            'volume': 'S_DQ_VOLUME',
            'turnover': 'S_DQ_AMOUNT',
            'preclose': 'S_DQ_PRECLOSE'
        }

        changed_field = fields.get(field)
        if changed_field:
            return changed_field
        else:
            return field

    def __int_remove_nan(self, value: str):  # str2int, 将NaN设为0
        if value != value:
            return 0
        else:
            return int(value)

    # close：当天收盘价  preclose：明天前收  foraf：明天复权因子
    def __get_forward_af(self, close: float, preclose: float, foraf: float):
        return round((preclose/close)*foraf, 5)  # 最多5位小数

    # price：当天价格
    def __forward_adjust_price(self, price: float, today_af: float, torm_af: float):
        return price*today_af/torm_af

    def __calculate_mtr(self, high: float, low: float, preclose: float):
        return max(high-low, abs(preclose-low), abs(high-preclose))

    '''
    RSI指标的计算公式：RSI = [上升平均数÷(上升平均数＋下跌平均数)]×100
    （其中，上升平均数是某一时期内升幅数的平均；而下跌平均数则是同一时期内跌幅数的平均）
    '''
    def __calculate_rsi(self, pctchanges: List[float]):
        down_sum = 0.0
        up_sum = 0.0
        down_num = 0
        up_num = 0

        for i in pctchanges:
            if i > 0:
                up_num = up_num + 1
                up_sum = up_sum + i
            if i < 0:
                down_num = down_num + 1
                down_sum = down_sum + i

        if up_num == 0:
            if down_num == 0:
                return np.nan
            return 0
        else:
            up_avg = up_sum/up_num
        if down_num == 0:
            return 100
        else:
            down_avg = down_sum/down_num

        return (up_avg/(up_avg+abs(down_avg)))*100

    def __get_end_date(self, symbol: str, freq: str, start_date):  # 获取不同freq下时间段的最后一天
        if freq == 'm':
            days_of_month = calendar.monthrange(start_date.year, start_date.month)[1]
            end_date = pd.Timestamp(start_date.year, start_date.month, days_of_month)

        if freq == 'q':
            end_month = start_date.month
            while end_month != 3 and end_month != 6 and end_month != 9 and end_month != 12:  # 判断开始日期所属季节的最后一月
                end_month = end_month + 1
            days_of_month = calendar.monthrange(start_date.year, end_month)[1]
            end_date = pd.Timestamp(start_date.year, end_month, days_of_month)

        if freq == 'h':
            if start_date.month <= 6:  # 判断开始日期属于上半年还是下半年
                end_date = pd.Timestamp(start_date.year, 6, 30)
            else:
                end_date = pd.Timestamp(start_date.year, 12, 31)

        if freq == 'y':
            end_date = pd.Timestamp(start_date.year, 12, 31)

        data = self.dataframes[symbol]
        timedelta = pd.Timedelta(days=1)
        while len(data[(data['TRADE_DT'] == end_date)].index) == 0:  # 该日期没有数据时，往前延一天
            end_date = end_date - timedelta

        return end_date

    def __get_date_by_freq(self, symbol: str, freq: str):  # 返回该freq下所有时间段的start_date和end_date
        output = pd.DataFrame(columns=('start', 'end'))
        data = self.dataframes[symbol]

        output.loc[0, 'start'] = data.loc[0, 'TRADE_DT']
        output.loc[0, 'end'] = self.__get_end_date(symbol, freq, output.loc[0, 'start'])

        data_rows = data.shape[0]
        output_rows = output.shape[0]

        while output.loc[output_rows-1, 'end'] != data.loc[data_rows-1, 'TRADE_DT']:
            last_end_index = data[(data['TRADE_DT'] == output.loc[output_rows-1, 'end'])].index[0]  # 上一个enddate即下一个startdate
            output = output.append(pd.Series({'start': output.loc[output_rows-1, 'end']}), ignore_index=True)
            output_rows = output.shape[0]
            output.loc[output_rows-1, 'end'] = self.__get_end_date(symbol, freq, data.loc[last_end_index+1, 'TRADE_DT'])  # 用startdate的下一天计算该freq下的enddate

        return output
