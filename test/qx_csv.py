import pandas as pd
import os


path = '/Users/liumeng/Downloads/'
missing_values = ["n/a", "na", "--"]

csv_path = os.path.join(path,'property-data.csv')
# df = pd.read_csv(csv_path, na_values=missing_values)
# print(df['NUM_BEDROOMS'])
# print(df['NUM_BEDROOMS'].isnull())
# df = pd.read_csv(csv_path)
# new_df = df.dropna()
# print(new_df)
# print(new_df.to_string)

# df.dropna(inplace = True)
#
# print(df.to_string())
# df = pd.read_csv('property-data.csv')

# df.dropna(subset=['ST_NUM'], inplace = True)
# df['PID'].fillna('12345',inplace=True)
# x = df['ST_NUM'].mean()
# y = df['ST_NUM'].median()
# z = df['ST_NUM'].mode()
# # print(x,y,z)
# print(x)
# df['ST_NUM'].fillna(x,inplace=True)
# print(df.to_string())

# data = {
#   "Date": ['2020/12/01', '2020/12/02', '20201226'],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data,index=['day1','day1','day3'])
# df['Date'] = pd.to_datetime(df['Date'])
# # print(df['Date'])
#
# person = {
#   "name": ['Google', 'Runoob','Runoob', 'Taobao'],
#   "age": [50, 40, 40, 23]    # 12345 年龄数据是错误的
# }
#
# df1 = pd.DataFrame(person)
# # df1.loc[2,'age']=30
# # print(df1.to_string)
# # for x in df1.index:
# #     if df1.loc[x,'age'] > 120:
# #         df1.drop(x, inplace = True)
# # print(df1.to_string)
# df1.drop_duplicates(inplace=True)
# print(df1.to_string)
# df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
# print(df.append(df2))

# d = {'Name':pd.Series(['c语言中文网','编程帮',"百度",'360搜索','谷歌','微学苑','Bing搜索']),
#    'years':pd.Series([5,6,15,28,3,19,23]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
# df = pd.DataFrame(d)
# df2 = pd.DataFrame()
# print(df)
# print(df.T)
# print(df.axes)
#
# # print(df.to_string)
# print(df.empty)
# print(df2.empty)
# print(df.ndim)
# print(df2.ndim)
# print(df.shape)
# print(df.size)
# print(df.values)


info= pd.DataFrame({'a_data': [40, 28, 39, 32, 18],
'b_data': [20, 37, 41, 35, 45],
'c_data': [22, 17, 11, 25, 15]})

print(info)
print(info.shift(periods=3))
print(info.shift(periods=3,axis=1,fill_value= 52)  )