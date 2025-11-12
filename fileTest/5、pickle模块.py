'''
pickle模块：
    作用：数据的持久化
    优势: 保持数据类型不变
'''

import pickle

# 写入数据
# data_01 = { "name": "张三", "age": 18 }
#
# with open(r"D:\project1110\fileTest\test_data", mode="wb") as fobj:
#     pickle.dump(data_01, fobj)


# 读取数据
with open(r"D:\project1110\fileTest\test_data", mode="rb") as fobj:
    data_02 = pickle.load(fobj)
    print(data_02)
    print(type(data_02))