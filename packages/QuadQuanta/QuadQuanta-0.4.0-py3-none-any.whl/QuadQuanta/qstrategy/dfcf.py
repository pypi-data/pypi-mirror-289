import requests
import pandas as pd
import json

# 东方财富股票行情接口URL
url = 'http://push2.eastmoney.com/api/qt/clist/get'

# 参数
params = {
    'pn': '0',           # 页数
    'pz': '5000',        # 每页数量（设定一个较大的值以获取所有股票）
    'po': '1',           # 排序方式
    'np': '1',           # 是否显示不同市场标识
    'ut': 'b2884a393a59ad64002292a3e90d46a5',
    'fltt': '2',         # 涨跌停价格限制
    'invt': '2',
    'fid': 'f3',         # 排序字段
    'fs': 'm:0+t:6,m:0+t:13',  # 沪深A股
    'fields': 'f12,f2,f3,f4,f5'
}

response = requests.get(url, params=params)
data = response.json()

# 解析数据
if data and 'data' in data and 'diff' in data['data']:
    stock_list = data['data']['diff']
    df = pd.DataFrame(stock_list)
    print(df)
else:
    print("No data retrieved")

# 保存到Excel
# df.to_excel('stock_data.xlsx', index=False)
