'''
数据类型： 数字、字符串、列表、元组、字典
数字：
    整数、浮点数、复数
'''

data_01 = 100
data_02 = 3.14
data_03 = 10 + 20j

print(type(data_01), type(data_02), type(data_03))

# 算术运算符： + - * / % ** // 地板除
print(10 + 4)
print(10 - 4)
print(10 * 4)
print(10 / 4)
print(10 % 4)
print(10 ** 4)
print(10 // 4)

# 不支持++， --, 支持 += -= *= /= %= **= //=
data_01 = 100
data_01 += 3
print(data_01)

# 比较运算符： > < >= <= == !=
print(10 > 4)
print(10 < 4)
print(10 >= 4)
print(10 <= 4)
print(10 == 4)
print(10 != 4)

# 逻辑运算符： and or not
print(10 > 4 and 10 < 20)
print(10 > 4 or 10 < 20)
print(not 10 < 20)

