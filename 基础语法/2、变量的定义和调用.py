# 定义变量  变量名称 = 值
'''
变量名称的规范：
    1、只能包含字母、数字、下划线
    2、只支持以字母或下划线开头
    3、变量名不能与python关键字冲突, if, for, def
    4、见名知义
'''
ip = "10.1.1.1"
name = "martin"
file = "/etc/fstab"

# 调用变量  变量名称
print(ip, name, file)

# 支持一行定义多个变量
user, password = "Admin", "123456"
print("用户名: %s, 密码: %s" % (user, password) )

# 交互式定义变量   变量名称 = input(提示信息)
# username = input("请输入用户名: ")
# print("用户名: %s" % username)

# input()默认的数据类型：字符串 str
# data_01 = input("测试数据: ")
# print(data_01)
# print(type(data_01))

data_01 = int(input("输入一个数字: "))
data_02 = int(input("再次输入一个数字: "))


print(data_01 + data_02)

