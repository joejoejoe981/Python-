import pandas as pd
import plotly.express as px
all_dataframe = pd.read_html('https://invest.cnyes.com/twstock/TWS/2330/history')
df = all_dataframe[0]
# 網頁中只有一個表格，取得串列第0項dataframe
print(df)
df.to_csv('stock.csv')
