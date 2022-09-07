import pandas as pd
import numpy as np

# d = {'Name':pd.Series(['小明','小亮','小红','小华','老赵','小曹','小陈',
#    '老李','老王','小冯','小何','老张']),
#    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
# }
# df = pd.DataFrame(d)
# print(df)
# print('*'*50)
# # print(df.sum())
# # print(df.sum(axis=1))
# # print(df['Age'].mean())
# print(df.describe())
# print('*'*50)
# print(df.describe(include=["object"]))
# print('*'*50)
# print(df.describe(include="all"))
# print('*'*50)

# df = pd.DataFrame(np.random.randn(5,3),columns=['coll1','coll2','coll3'])
# print(df)
# print('*'*50)
# print(df.applymap(lambda x:x*10))
# print(df.apply(np.mean))
# print(df['coll1'].map(lambda x:x*100))
# print(df.apply(lambda x: x.max() - x.min()))

# N=20
# df = pd.DataFrame({
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
# })
# print(df)
# df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
# print(df_reindexed)
# df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
# print (df1)
# print (df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))

# N=20
# df = pd.DataFrame({
#    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
#    'x': np.linspace(0,stop=N-1,num=N),
#    'y': np.random.rand(N),
#    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
#    'D': np.random.normal(100, 10, size=(N)).tolist()
#    })
# print(df)
# for col in df:
#    print (col)
# df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
# print(df)
# for key,value in df.iteritems():
#    print (key,value)


# df = pd.DataFrame(np.random.randn(3,3),columns = ['col1','col2','col3'])
# print(df)
# for row_index,row in df.iterrows():
# #     print(row_index,row)
# df = pd.DataFrame(np.random.randn(3,3),columns = ['col1','col2','col3'])
# for index, row in df.iterrows():
#    row['a'] = 15
# print(df)
# unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,6,4,2,3,5,9,8,0,7],columns=['col2','col1'])
# sorted_df = unsorted_df.sort_index(ascending=False)
# print(unsorted_df)
# print('*'*50)
# # print(unsorted_df.sort_index())
# print(sorted_df)
# unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
# print(unsorted_df)
# sorted_coll = unsorted_df.sort_values(by='col1')
# print(sorted_coll)
# sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')
# print(sorted_df)
data = {

    'A': [1, 3, 3, 3],
    'B': [0, 1, 2, 0],
    'C': [4, 5, 4, 4],
    'D': [3, 3, 3, 3]
}
df = pd.DataFrame(data=data)
print(df)
# print(df.drop_duplicates())
