# -*- coding: utf-8 -*-
import adata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getData(code):
    print(adata.version())
    # 代理
    adata.proxy(False)

    # k线行情数据:"时间戳", "时间","开盘","收盘","成交量","最高","最低","成交额","涨跌额","涨跌幅","换手率","昨收"
    res_df = adata.stock.market.get_market(stock_code=code, k_type=1, start_date='2023-11-01')
    print(res_df.describe())
    res_df.to_csv("res.txt", sep=',', index=True)
    print(res_df)

def getVolume(df):
    # Fixing random state for reproducibility
    np.random.seed(19680801)
    plt.figure(figsize=(10, 6))
    # df.set_index('trade_time', inplace=True)

    #plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['red', 'blue', 'green', 'yellow'])

    # 假设你有一个DataFrame df
    df['volume'] = (df['volume'] - df['volume'].min()) / (df['volume'].max() - df['volume'].min())
    df['high'] = (df['high'] - df['high'].min()) / (df['high'].max() - df['high'].min())

    plt.plot( df['trade_time'], df['volume'], marker='o', linestyle='-', color='r')  # 绘制折线图，带圆圈标记

    plt.plot( df['trade_time'], df['high'], marker='o', linestyle='-', color='b')  # 绘制折线图，带圆圈标记
    plt.title('Line Plot of Value1 and Value2 - how2matplotlib.com')
    plt.xlabel('trade_time')
    plt.ylabel('volume')
    plt.legend()
    plt.show()

def test():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    # 创建示例数据
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=10),
        'Value1': np.random.rand(10) * 100,
        'Value2': np.random.rand(10) * 50,
        'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']
    }
    df = pd.DataFrame(data)
    df.set_index('Date', inplace=True)

    plt.figure(figsize=(10, 6))
    df[['Value1', 'Value2']].plot(kind='line')
    print(df)
    plt.title('Line Plot of Value1 and Value2 - how2matplotlib.com')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    getData('000158')
    #test()
    res_df = pd.read_csv('res.txt')
    # 成交量volume
    print(type(res_df))
    print(res_df)
    getVolume(res_df)


