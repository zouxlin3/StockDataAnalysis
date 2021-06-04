# 介绍
项目地址 https://github.com/zouxlin3/StockDataAnalysis
使用python分析csv格式的股票数据
使用方法如下


```python
from StockData import StockData  # 从源代码下载StockData.py和666666.SZ.csv虚拟数据
```

# 1 读取csv
虚拟数据的股票代码为000001
每个股票代码应对应一个csv文件
read(symbols: List[str])


```python
stockdata = StockData('data')  # 虚拟数据文件所在目录
symbols = ['000001']  # symbols为股票代码列表
stockdata.read(symbols)
stockdata.dataframes['000001']  # 查看内容
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>OBJECT_ID</th>
      <th>S_INFO_WINDCODE</th>
      <th>TRADE_DT</th>
      <th>CRNCY_CODE</th>
      <th>S_DQ_PRECLOSE</th>
      <th>S_DQ_OPEN</th>
      <th>S_DQ_HIGH</th>
      <th>S_DQ_LOW</th>
      <th>S_DQ_CLOSE</th>
      <th>...</th>
      <th>S_DQ_ADJPRECLOSE</th>
      <th>S_DQ_ADJOPEN</th>
      <th>S_DQ_ADJHIGH</th>
      <th>S_DQ_ADJLOW</th>
      <th>S_DQ_ADJCLOSE</th>
      <th>S_DQ_ADJFACTOR</th>
      <th>S_DQ_AVGPRICE</th>
      <th>S_DQ_TRADESTATUS</th>
      <th>OPDATE</th>
      <th>OPMODE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>336601</td>
      <td>-488126</td>
      <td>000001.SZ</td>
      <td>1991-04-03</td>
      <td>CNY</td>
      <td>61.49</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>...</td>
      <td>61.49</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>1.000000</td>
      <td>50.0000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>336602</td>
      <td>-488127</td>
      <td>000001.SZ</td>
      <td>1991-04-04</td>
      <td>CNY</td>
      <td>49.00</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>...</td>
      <td>49.00</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>1.000000</td>
      <td>50.0000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>336603</td>
      <td>-488128</td>
      <td>000001.SZ</td>
      <td>1991-04-05</td>
      <td>CNY</td>
      <td>48.76</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>...</td>
      <td>48.76</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>1.000000</td>
      <td>50.0000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>336605</td>
      <td>-488130</td>
      <td>000001.SZ</td>
      <td>1991-04-08</td>
      <td>CNY</td>
      <td>48.52</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>...</td>
      <td>48.52</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>1.000000</td>
      <td>50.0000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>336606</td>
      <td>-488131</td>
      <td>000001.SZ</td>
      <td>1991-04-09</td>
      <td>CNY</td>
      <td>48.04</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>...</td>
      <td>48.04</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>1.000000</td>
      <td>47.5000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6298</th>
      <td>6864894</td>
      <td>{D1A958FC-E2CC-11E6-9220-6C0B84A6895D}</td>
      <td>000001.SZ</td>
      <td>2017-01-25</td>
      <td>CNY</td>
      <td>9.27</td>
      <td>9.27</td>
      <td>9.28</td>
      <td>9.25</td>
      <td>9.26</td>
      <td>...</td>
      <td>971.11</td>
      <td>971.11</td>
      <td>972.16</td>
      <td>969.01</td>
      <td>970.06</td>
      <td>104.758253</td>
      <td>9.2633</td>
      <td>??</td>
      <td>2017-01-25 15:10:52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6299</th>
      <td>1717817</td>
      <td>{1930026C-E396-11E6-9CA9-4437E6DAC6D1}</td>
      <td>000001.SZ</td>
      <td>2017-01-26</td>
      <td>CNY</td>
      <td>9.26</td>
      <td>9.27</td>
      <td>9.34</td>
      <td>9.26</td>
      <td>9.33</td>
      <td>...</td>
      <td>970.06</td>
      <td>971.11</td>
      <td>978.44</td>
      <td>970.06</td>
      <td>977.39</td>
      <td>104.758253</td>
      <td>9.3138</td>
      <td>??</td>
      <td>2017-01-26 15:26:14</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6300</th>
      <td>3288514</td>
      <td>{518B8FC9-E9DF-11E6-84F4-6C0B84A6895D}</td>
      <td>000001.SZ</td>
      <td>2017-02-03</td>
      <td>CNY</td>
      <td>9.33</td>
      <td>9.34</td>
      <td>9.36</td>
      <td>9.23</td>
      <td>9.26</td>
      <td>...</td>
      <td>977.39</td>
      <td>978.44</td>
      <td>980.54</td>
      <td>966.92</td>
      <td>970.06</td>
      <td>104.758253</td>
      <td>9.2756</td>
      <td>??</td>
      <td>2017-02-03 15:09:52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6301</th>
      <td>6878988</td>
      <td>{D21CCA60-EC3A-11E6-85F7-6C0B84A6895D}</td>
      <td>000001.SZ</td>
      <td>2017-02-06</td>
      <td>CNY</td>
      <td>9.26</td>
      <td>9.26</td>
      <td>9.32</td>
      <td>9.26</td>
      <td>9.31</td>
      <td>...</td>
      <td>970.06</td>
      <td>970.06</td>
      <td>976.35</td>
      <td>970.06</td>
      <td>975.30</td>
      <td>104.758253</td>
      <td>9.2967</td>
      <td>??</td>
      <td>2017-02-06 15:20:12</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6302</th>
      <td>1204979</td>
      <td>{0700EF99-ED04-11E6-A728-6C0B84A6895D}</td>
      <td>000001.SZ</td>
      <td>2017-02-07</td>
      <td>CNY</td>
      <td>9.31</td>
      <td>9.31</td>
      <td>9.32</td>
      <td>9.27</td>
      <td>9.30</td>
      <td>...</td>
      <td>975.30</td>
      <td>975.30</td>
      <td>976.35</td>
      <td>971.11</td>
      <td>974.25</td>
      <td>104.758253</td>
      <td>9.2912</td>
      <td>??</td>
      <td>2017-02-07 15:12:19</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>6303 rows × 24 columns</p>
</div>



# 2 根据条件查看数据

## 2.1 根据时间段查看
查看一个股票在时间段的open high low close四个标签的数据
get_data_by_symbol(symbol: str, start_date: str, end_date: str)


```python
stockdata.get_data_by_symbol('000001', '19910409', '19910419')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>1991-04-09</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>47.80</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1991-04-10</td>
      <td>47.56</td>
      <td>47.56</td>
      <td>47.56</td>
      <td>47.56</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1991-04-11</td>
      <td>47.56</td>
      <td>47.56</td>
      <td>47.56</td>
      <td>47.56</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1991-04-12</td>
      <td>47.08</td>
      <td>47.08</td>
      <td>47.08</td>
      <td>47.08</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1991-04-16</td>
      <td>46.38</td>
      <td>46.38</td>
      <td>46.38</td>
      <td>46.38</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1991-04-17</td>
      <td>46.15</td>
      <td>46.15</td>
      <td>46.15</td>
      <td>46.15</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1991-04-18</td>
      <td>45.92</td>
      <td>45.92</td>
      <td>45.92</td>
      <td>45.92</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1991-04-19</td>
      <td>45.69</td>
      <td>45.69</td>
      <td>45.69</td>
      <td>45.69</td>
    </tr>
  </tbody>
</table>
</div>



## 2.2 根据时间段查看
查看指定日期一些股票的open high low close四个标签的数据
get_data_by_date( adate: str, symbols: List[str])


```python
stockdata.get_data_by_date('20170207', symbols)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symbols</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>000001</td>
      <td>9.31</td>
      <td>9.32</td>
      <td>9.27</td>
      <td>9.3</td>
    </tr>
  </tbody>
</table>
</div>



## 2.3 根据时间段查看
查看一些股票指定标签的数据
get_data_by_field(field: str, symbols: List[str])


```python
stockdata.get_data_by_field('open', symbols)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>000001</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1991-04-03</td>
      <td>49.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1991-04-04</td>
      <td>48.76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1991-04-05</td>
      <td>48.52</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1991-04-08</td>
      <td>48.04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1991-04-09</td>
      <td>47.80</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6298</th>
      <td>2017-01-25</td>
      <td>9.27</td>
    </tr>
    <tr>
      <th>6299</th>
      <td>2017-01-26</td>
      <td>9.27</td>
    </tr>
    <tr>
      <th>6300</th>
      <td>2017-02-03</td>
      <td>9.34</td>
    </tr>
    <tr>
      <th>6301</th>
      <td>2017-02-06</td>
      <td>9.26</td>
    </tr>
    <tr>
      <th>6302</th>
      <td>2017-02-07</td>
      <td>9.31</td>
    </tr>
  </tbody>
</table>
<p>6303 rows × 2 columns</p>
</div>



# 3 绘制走势图
需要指定一个标签，volume和turnover标签时绘制柱状图，其余为折线图
plot(symbol: str, field: str)


```python
stockdata.plot('000001', 'open')
```


![image](https://img2020.cnblogs.com/blog/2389253/202106/2389253-20210604205022353-1721983562.png)


# 4 数据处理

# 4.1 价格复权计算
对open high low close四类价格从后往前复权
adjust_data(symbol: str)


```python
stockdata.adjust_data('000001')
stockdata.dataframes['000001']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>OBJECT_ID</th>
      <th>S_INFO_WINDCODE</th>
      <th>TRADE_DT</th>
      <th>CRNCY_CODE</th>
      <th>S_DQ_PRECLOSE</th>
      <th>S_DQ_OPEN</th>
      <th>S_DQ_HIGH</th>
      <th>S_DQ_LOW</th>
      <th>S_DQ_CLOSE</th>
      <th>...</th>
      <th>S_DQ_ADJFACTOR</th>
      <th>S_DQ_AVGPRICE</th>
      <th>S_DQ_TRADESTATUS</th>
      <th>OPDATE</th>
      <th>OPMODE</th>
      <th>forward_af</th>
      <th>forward_adjust_open</th>
      <th>forward_adjust_high</th>
      <th>forward_adjust_low</th>
      <th>forward_adjust_close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>336601</td>
      <td>-488126</td>
      <td>000001.SZ</td>
      <td>1991-04-03</td>
      <td>CNY</td>
      <td>61.49</td>
      <td>49</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>...</td>
      <td>1.000000</td>
      <td>50.0000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
      <td>0.01051</td>
      <td>49.0</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>49.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>336602</td>
      <td>-488127</td>
      <td>000001.SZ</td>
      <td>1991-04-04</td>
      <td>CNY</td>
      <td>49.00</td>
      <td>48</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>...</td>
      <td>1.000000</td>
      <td>50.0000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
      <td>0.01051</td>
      <td>48.0</td>
      <td>48.76</td>
      <td>48.76</td>
      <td>48.76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>336603</td>
      <td>-488128</td>
      <td>000001.SZ</td>
      <td>1991-04-05</td>
      <td>CNY</td>
      <td>48.76</td>
      <td>48</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>...</td>
      <td>1.000000</td>
      <td>50.0000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
      <td>0.01051</td>
      <td>48.0</td>
      <td>48.52</td>
      <td>48.52</td>
      <td>48.52</td>
    </tr>
    <tr>
      <th>3</th>
      <td>336605</td>
      <td>-488130</td>
      <td>000001.SZ</td>
      <td>1991-04-08</td>
      <td>CNY</td>
      <td>48.52</td>
      <td>48</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>...</td>
      <td>1.000000</td>
      <td>50.0000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
      <td>0.01051</td>
      <td>48.0</td>
      <td>48.04</td>
      <td>48.04</td>
      <td>48.04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>336606</td>
      <td>-488131</td>
      <td>000001.SZ</td>
      <td>1991-04-09</td>
      <td>CNY</td>
      <td>48.04</td>
      <td>47</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>...</td>
      <td>1.000000</td>
      <td>47.5000</td>
      <td>??</td>
      <td>2016-12-27 10:24:33</td>
      <td>0</td>
      <td>0.01051</td>
      <td>47.0</td>
      <td>47.80</td>
      <td>47.80</td>
      <td>47.80</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6298</th>
      <td>6864894</td>
      <td>{D1A958FC-E2CC-11E6-9220-6C0B84A6895D}</td>
      <td>000001.SZ</td>
      <td>2017-01-25</td>
      <td>CNY</td>
      <td>9.27</td>
      <td>9</td>
      <td>9.28</td>
      <td>9.25</td>
      <td>9.26</td>
      <td>...</td>
      <td>104.758253</td>
      <td>9.2633</td>
      <td>??</td>
      <td>2017-01-25 15:10:52</td>
      <td>0</td>
      <td>1.00000</td>
      <td>9.0</td>
      <td>9.28</td>
      <td>9.25</td>
      <td>9.26</td>
    </tr>
    <tr>
      <th>6299</th>
      <td>1717817</td>
      <td>{1930026C-E396-11E6-9CA9-4437E6DAC6D1}</td>
      <td>000001.SZ</td>
      <td>2017-01-26</td>
      <td>CNY</td>
      <td>9.26</td>
      <td>9</td>
      <td>9.34</td>
      <td>9.26</td>
      <td>9.33</td>
      <td>...</td>
      <td>104.758253</td>
      <td>9.3138</td>
      <td>??</td>
      <td>2017-01-26 15:26:14</td>
      <td>0</td>
      <td>1.00000</td>
      <td>9.0</td>
      <td>9.34</td>
      <td>9.26</td>
      <td>9.33</td>
    </tr>
    <tr>
      <th>6300</th>
      <td>3288514</td>
      <td>{518B8FC9-E9DF-11E6-84F4-6C0B84A6895D}</td>
      <td>000001.SZ</td>
      <td>2017-02-03</td>
      <td>CNY</td>
      <td>9.33</td>
      <td>9</td>
      <td>9.36</td>
      <td>9.23</td>
      <td>9.26</td>
      <td>...</td>
      <td>104.758253</td>
      <td>9.2756</td>
      <td>??</td>
      <td>2017-02-03 15:09:52</td>
      <td>0</td>
      <td>1.00000</td>
      <td>9.0</td>
      <td>9.36</td>
      <td>9.23</td>
      <td>9.26</td>
    </tr>
    <tr>
      <th>6301</th>
      <td>6878988</td>
      <td>{D21CCA60-EC3A-11E6-85F7-6C0B84A6895D}</td>
      <td>000001.SZ</td>
      <td>2017-02-06</td>
      <td>CNY</td>
      <td>9.26</td>
      <td>9</td>
      <td>9.32</td>
      <td>9.26</td>
      <td>9.31</td>
      <td>...</td>
      <td>104.758253</td>
      <td>9.2967</td>
      <td>??</td>
      <td>2017-02-06 15:20:12</td>
      <td>0</td>
      <td>1.00000</td>
      <td>9.0</td>
      <td>9.32</td>
      <td>9.26</td>
      <td>9.31</td>
    </tr>
    <tr>
      <th>6302</th>
      <td>1204979</td>
      <td>{0700EF99-ED04-11E6-A728-6C0B84A6895D}</td>
      <td>000001.SZ</td>
      <td>2017-02-07</td>
      <td>CNY</td>
      <td>9.31</td>
      <td>9</td>
      <td>9.32</td>
      <td>9.27</td>
      <td>9.30</td>
      <td>...</td>
      <td>104.758253</td>
      <td>9.2912</td>
      <td>??</td>
      <td>2017-02-07 15:12:19</td>
      <td>0</td>
      <td>1.00000</td>
      <td>9.0</td>
      <td>9.32</td>
      <td>9.27</td>
      <td>9.30</td>
    </tr>
  </tbody>
</table>
<p>6303 rows × 29 columns</p>
</div>



# 4.2 日频数据重采样
按照时间窗口进行重采样，采样的时间取区间左端
resample(symbol: str, freq: int)


```python
stockdata.resample('000001', 5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>volume</th>
      <th>turnover</th>
      <th>vwap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1991-04-09</td>
      <td>49</td>
      <td>47.80</td>
      <td>49.00</td>
      <td>47.80</td>
      <td>12.0</td>
      <td>59.000</td>
      <td>4.9167</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1991-04-17</td>
      <td>47</td>
      <td>46.15</td>
      <td>47.56</td>
      <td>46.15</td>
      <td>26.0</td>
      <td>123.000</td>
      <td>4.7308</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1991-04-24</td>
      <td>45</td>
      <td>44.78</td>
      <td>45.92</td>
      <td>44.78</td>
      <td>50.0</td>
      <td>225.000</td>
      <td>4.5000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1991-05-02</td>
      <td>44</td>
      <td>43.46</td>
      <td>44.56</td>
      <td>43.46</td>
      <td>31.0</td>
      <td>137.000</td>
      <td>4.4194</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1991-05-09</td>
      <td>43</td>
      <td>42.17</td>
      <td>43.24</td>
      <td>42.17</td>
      <td>129.0</td>
      <td>546.000</td>
      <td>4.2326</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1255</th>
      <td>2016-12-28</td>
      <td>9</td>
      <td>9.06</td>
      <td>9.16</td>
      <td>9.02</td>
      <td>1631209.0</td>
      <td>1483308.481</td>
      <td>0.9093</td>
    </tr>
    <tr>
      <th>1256</th>
      <td>2017-01-05</td>
      <td>9</td>
      <td>9.17</td>
      <td>9.18</td>
      <td>9.05</td>
      <td>1894909.0</td>
      <td>1729934.514</td>
      <td>0.9129</td>
    </tr>
    <tr>
      <th>1257</th>
      <td>2017-01-12</td>
      <td>9</td>
      <td>9.15</td>
      <td>9.17</td>
      <td>9.11</td>
      <td>1691727.0</td>
      <td>1547168.777</td>
      <td>0.9145</td>
    </tr>
    <tr>
      <th>1258</th>
      <td>2017-01-19</td>
      <td>9</td>
      <td>9.18</td>
      <td>9.24</td>
      <td>9.07</td>
      <td>2675002.0</td>
      <td>2447679.663</td>
      <td>0.9150</td>
    </tr>
    <tr>
      <th>1259</th>
      <td>2017-01-26</td>
      <td>9</td>
      <td>9.33</td>
      <td>9.34</td>
      <td>9.17</td>
      <td>2008986.0</td>
      <td>1858492.536</td>
      <td>0.9251</td>
    </tr>
  </tbody>
</table>
<p>1260 rows × 8 columns</p>
</div>



# 4.3 计算移动平均
计算滑动窗口内数据的平均值
moving_average(symbol: str, field: str, window: int)


```python
stockdata.moving_average('000001', 'open', 5)
```




    TRADE_DT
    1991-04-03     NaN
    1991-04-04     NaN
    1991-04-05     NaN
    1991-04-08     NaN
    1991-04-09    48.0
                  ... 
    2017-01-25     9.0
    2017-01-26     9.0
    2017-02-03     9.0
    2017-02-06     9.0
    2017-02-07     9.0
    Name: forward_adjust_open, Length: 6303, dtype: float64



# 5 相关指标计算
四类指标
ema(symbol: str, periods: int)
atr(symbol: str, periods: int)
rsi(symbol: str, periods: int)
macd(symbol: str, long: int, short: int, dea_periods: int)


```python
stockdata.ema('000001', 5)
```




    TRADE_DT
    1991-04-03          NaN
    1991-04-04          NaN
    1991-04-05          NaN
    1991-04-08          NaN
    1991-04-09    49.500000
                    ...    
    2017-01-25     9.233294
    2017-01-26     9.265529
    2017-02-03     9.263686
    2017-02-06     9.279124
    2017-02-07     9.286083
    Name: ema_5, Length: 6303, dtype: float64




```python
stockdata.atr('000001', 5)
```




    TRADE_DT
    1991-04-03      NaN
    1991-04-04      NaN
    1991-04-05      NaN
    1991-04-08      NaN
    1991-04-09    2.738
                  ...  
    2017-01-25    0.064
    2017-01-26    0.062
    2017-02-03    0.076
    2017-02-06    0.076
    2017-02-07    0.070
    Name: atr_5, Length: 6303, dtype: float64




```python
stockdata.rsi('000001', 5)
```




    TRADE_DT
    1991-04-03          NaN
    1991-04-04          NaN
    1991-04-05          NaN
    1991-04-08          NaN
    1991-04-09          NaN
                    ...    
    2017-01-25    75.156853
    2017-01-26    81.025235
    2017-02-03    57.391103
    2017-02-06    58.812990
    2017-02-07    65.561024
    Name: rsi_5, Length: 6303, dtype: float64




```python
stockdata.macd('000001', 25, 9, 5)
```




    TRADE_DT
    1991-04-03         NaN
    1991-04-04         NaN
    1991-04-05         NaN
    1991-04-08         NaN
    1991-04-09         NaN
                    ...   
    2017-01-25    0.017994
    2017-01-26    0.021877
    2017-02-03    0.014808
    2017-02-06    0.013298
    2017-02-07    0.010009
    Name: macd, Length: 6303, dtype: float64



# 6 回报计算
freq可选m、q、h、y，分别代表月、季度、半年、年的时间跨频率

# 6.1 回报率
calc_return(symbol: str, freq: str)


```python
stockdata.calc_return('000001', 'q')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>return_q</th>
      <th>return</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1991-06-28</td>
      <td>NaT</td>
      <td>-30.6327</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1991-09-30</td>
      <td>NaT</td>
      <td>-57.0462</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1991-12-31</td>
      <td>NaT</td>
      <td>101.0274</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1992-03-31</td>
      <td>NaT</td>
      <td>-11.2436</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1992-06-30</td>
      <td>NaT</td>
      <td>61.2284</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>99</th>
      <td>2016-03-31</td>
      <td>NaT</td>
      <td>-11.2594</td>
    </tr>
    <tr>
      <th>100</th>
      <td>2016-06-30</td>
      <td>NaT</td>
      <td>-18.2331</td>
    </tr>
    <tr>
      <th>101</th>
      <td>2016-09-30</td>
      <td>NaT</td>
      <td>4.2529</td>
    </tr>
    <tr>
      <th>102</th>
      <td>2016-12-30</td>
      <td>NaT</td>
      <td>0.3308</td>
    </tr>
    <tr>
      <th>103</th>
      <td>2017-02-07</td>
      <td>NaT</td>
      <td>2.1978</td>
    </tr>
  </tbody>
</table>
<p>104 rows × 3 columns</p>
</div>



# 6.2 夏普比率
calc_sharpe_ratio(symbol: str, freq: str)


```python
stockdata.calc_sharpe_ratio('000001', 'q')
```




    0.04988574991791399



# 6.3 最大回撤率
calc_max_drawdown_ratio(symbol: str)


```python
stockdata.calc_max_drawdown_ratio('000001')
```




    91.63934426229508



# [本文最新版本](https://www.cnblogs.com/zouxlin3/p/14851297.html)
