'''
操作文件流程：
1、打开文件, 创建文件对象   open(文件名称、模式)
    模式:   r(默认)、w(写入、新建文件)
2、读写操作
3、关闭文件
'''

test_file = r"D:\python\fileTest\test.txt"

# fobj = open(test_file, mode="r")
#
# content = fobj.read()
# print(content)
# print(type(content))
#
# fobj.close()

# -------- 遍历文件内容, 按行读取 --------------

# fobj = open(test_file, mode="r")
#
# for line in fobj:
#     print("行: ", line)
#
# fobj.close()


# -------- with 关键字 --------------
with open(test_file, mode="r") as fobj:
    for line in fobj:
        print("行: ", line)

print("文件是否关闭: ", fobj.closed)