# 输出语句  print("内容")
print("hello world")
print("hello, Linux自动化运维")
print("hello, Python")


# 引号的使用， 双引号， 单引号
print('黄鹤楼')
print("update 表名 set name='martin'")
print('name')
print("中文")

# 变量的使用，调用变量 变量名称
ip = "192.168.10.1"
print(ip)
name= "Linux"
print(name)


# 服务器地址: 192.168.10.1
print("服务器地址: ",  ip)
print("服务器名称: ", name)

# 字符串拼接   delete from 表名 where ip='192.168.10.1'
# 字符串拼接， 占位符  %s  字符串占位
print("delete from 表名 where ip='%s'" % ip)
print("delete from 表名 where name='%s'" % name)

ip = "10.1.1.1"
username = "martin"
port = 22345
user = "xiao"
print("服务器地址: %s, 登录的用户: %s" % (ip, username))
print("用户: %s, 端口: %s" % (user, port))


# 占位符： %d， 整数
print("数字1: %d" % 789)
print("数字1: %d" % 3.1415926)
print("ssh %s@%s -p %d" % (username, ip, port))

# 占位符: %f   浮点数
print("数字1: %f" % 3.14)
print("数字1: %f" % 3.1415926234324)
print("数字1: %.3f" % 3.1415926234324)

