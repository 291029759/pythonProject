import pandas as pd
import os
import json
from glom import glom


# print(pd.__version__ )
# mydataset = {
#   'sites': ["Google", "Runoob", "Wiki"],
#   'number': [1, 2, '']
# }
# myvar = pd.DataFrame(mydataset)
#
# a = [1,2,3]
# b = ["Google", "Runoob", "Wiki"]
# myvar1 = pd.Series(a)
# myvar2 = pd.Series(b,index=['x','y','z'])
# # print(myvar2)
# data = {
#   "mango": [420, 380, 390],
#   "apple": [50, 40, 45],
#   "pear": [1, 2, 3],
#   "banana": [23, 45,56]
# }
# df = pd.DataFrame(data)
# # print(df[])
# # print(df[["apple","banana"]])
path = '/Users/liumeng/Downloads/'
# df = pd.read_csv(path)
# print(df.to_string())
# print(df)
# nme = ["Google", "Runoob", "Taobao", "Wiki"]
# st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
# ag = [90, 40, 80, 98]
# dict = {'name': nme,'site': st,'age':ag}
# df = pd.DataFrame(dict)
# df.to_csv('/Users/liumeng/Downloads/site.csv')
# print(df.head(10))
# print(df.tail(5))
# print(df.info())
# json_path = os.path.join(path,'sites.json')
# df = pd.read_json(json_path)
data =[
    {
      "id": "A001",
      "name": "菜鸟教程",
      "url": "www.runoob.com",
      "likes": 61
    },
    {
      "id": "A002",
      "name": "Google",
      "url": "www.google.com",
      "likes": 124
    },
    {
      "id": "A003",
      "name": "淘宝",
      "url": "www.taobao.com",
      "likes": 45
    }
]


s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# URL = 'https://static.runoob.com/download/sites.json'
# df = pd.DataFrame(s)
# df = pd.read_json(URL)
# df = pd.read_json('nested_list.json')

# print(df)
# with open('nested_deep.json.json', 'r') as f:
#     data = json.loads(f.read())

df = pd.read_json('nested_deep.json')
data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)

'''df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)'''

# df_nested_list = pd.json_normalize(data,record_path=['students'],meta=['school_name','class'])
# df = pd.json_normalize(
#     data,
#     record_path = ['students'],
#     meta= ['class',
#         ['info','president'],
#         ['info', 'contacts', 'tel'],
#         ['info', 'contacts', 'email']
#
# ])
# print(df)