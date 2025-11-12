'''
异常捕获：
     作用：将代码可能发生的报警捕获下来，使用自己的操作来替换程序本身的报错

异常捕获的语法: try ... expect

try:
    关键性代码
except 异常名称 as e:
    执行操作
except 异常名称 as e:
'''
import sys

filename = input("文件名称: ").strip()
filemode= input("操作模式: ").strip()

try:
    fobj = open(filename, mode=filemode)
except FileNotFoundError as e:
    print("文件不存在,请检查文件路径是否存在")
    print(e)
    sys.exit()
except ValueError as e:
    print("操作模式错误")
    print(e)
    sys.exit()

content = fobj.read()
print(content)