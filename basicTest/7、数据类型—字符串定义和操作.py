# 字符串定义：定义在一对引号的数据
data_01 = ""
data_02 = "192.168.10.1"

print(type(data_01), type(data_02))

# 原始 raw 字符串, 避免特殊字符转义
win_file_name = r"D:\newdir\test\logo.jpg"
print(win_file_name)

#-------字符串操作符--------------

# 1、字符串拼接  +
print("Ab" + "CD")

# 2、字符串重复  *
print("---------------" * 4)

# 3、获取字符串长度    len()
print(len("Hello"))

# 4、判断字符串包含关系, in, not in
print("el" in "hello")
print("el" not in "hello")

# 5、字符串索引    字符串[下标]， 从左：0， 从右：-1
data_01 = "Linux"

print(data_01[0])
print(data_01[-2])

# 6、字符串切片   字符串[起始下标:终止下标:步长]   默认起始：0， 默认终止：-1， 默认步长：1
data_01 = 'Linux'

print(data_01[0:3])
print(data_01[3:])

# 7、字符串倒置
print(data_01[::-1])

# --------- 字符串对象的操作方法 ----------------------

# 1、转换大小写
print("aBcD".upper())
print("aBcD".lower())
print("aBcD".capitalize())

# 2、判断字符串的开头、结尾
print("Linux".startswith("Lin"))
print("Linux".endswith("x"))

# 3、删除字符串左、右两侧的空白
data_01 = "        Linux    "
print(data_01.strip())
print(data_01.lstrip())
print(data_01.rstrip())

# 4、split() 分割字符串，默认空白
data_01 = "nginx  java   tomcat  redis"
new_data_01 = data_01.split()
print(new_data_01)
print(new_data_01[-2])

ip = "192.168.32.52"
new_ip = ip.split(".")
print(new_ip)
print(new_ip[-3])
print(type(new_ip[-3]))

# 5、判断字符串的组成结构
print("12332523".isdigit())
print("PYTHON".isupper())

# 6、字符串替换
file_name = "/etc/sysconfig/network-scripts/ifcfg-eth0"
new_file_name = file_name.replace("eth0", "ens33")
print(new_file_name)



choice = input("执行/取消[Y/N]? ").upper().strip()

if choice == "Y":
    print("执行操作")
else:
    print("取消操作")


