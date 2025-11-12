# os.walk(目录), 递归获取目录下的文件信息

directory = r"D:\python\fileTest\北京"

import os

# 直接返回的生成器
result = os.walk(directory)

print(result)

# 遍历生成器，查看实际的数据
# for i in result:
#     print(i)

print("------------------------------")

# for i in result:
#     print("目录名称: %s" % i[0])
#     print("对应的文件: %s" % i[-1])

print("------------------------------")

for i, j, k in result:
    print("目录名称: %s" % i)
    print("对应的文件: %s" % k)

# os.rename(r"D:\project1110\fileTest\北京\a.txt", r"D:\project1110\fileTest\北京\aaa.txt")

# 获取文件的创建时间
file_name = r"D:\python\fileTest\北京\福兴苑\d_2025_11_12.txt"

import os
# 时间戳
create_time = os.path.getctime(file_name)
print(create_time)

# 时间格式转换
import datetime
new_create_time = datetime.datetime.fromtimestamp(create_time).strftime("%Y_%m_%d")
print(new_create_time)

