import pandas as pd

# print('不適合plotly資料格式')
# data = dict(月份 = ["Jan","Feb","Mar"],台積電 = [1,2,3])
# wide_df = pd.DataFrame(data)
# print(wide_df)

#
# print('不適合plotly資料格式')
# data = dict(月份 = ["Jan","Feb","Mar"],台積電 = [1,2,3])
# wide_df = pd.DataFrame(data)
# print(wide_df)
# print('整理後')
# tidy_df = wide_df.melt(id_vars='月份')
# print(tidy_df)

print('不適合plotly資料格式')
data = dict(月份 = ["Jan","Feb","Mar"],台積電 = [1,2,3])
wide_df = pd.DataFrame(data)
print(wide_df)
print('整理後')
tidy_df = wide_df.melt(id_vars='月份')
print(tidy_df)
print('整理後並設定欄位名稱')
tidy_df = wide_df.melt(id_vars="月份",var_name='個股名稱',value_name='成交張數')
print(tidy_df)