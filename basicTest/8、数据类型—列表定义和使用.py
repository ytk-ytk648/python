# 列表定义：定义在一对方括号[]中的数据, [ 元素, 元素, 元素 ]
# 支持存储任意类型的数据

data_01 = []
data_02 = [ 1, 2, 3, 4, 5 ]
data_03 = [ "docker", "k8s", "harbor" ]
data_04 = [ ["docker", "26.1"], ["k8s", "1.29"] ]

print(type(data_01), type(data_02), type(data_03), type(data_04))

# 列表解析, 快速生成列表，测试数据
data_05 = [ i for i in range(1, 11) ]
print(data_05)

data_06 = [ i ** 2 for i in range(1, 11) if i % 2 ]
print(data_06)

data_07 = [ "192.168.1.%s" % i for i in range(1, 11) ]
print(data_07)


# -------------------- 列表操作符 ----------------------------
# 1、获取长度 len()
data_03 = [ "docker", "k8s", "harbor" ]
data_04 = [ ["docker", "26.1"], ["k8s", "1.29"] ]

print(len(data_03), len(data_04))

# 2、判断成员包含关系 in, not in
print("docker" in data_03)
print(["docker", "26.1"] in data_04)

# 3、索引
print(data_03[0])
print(data_04[0])
print(data_04[-1][-1])

data_03 = [ "docker", "k8s", "harbor" ]

# 列表是可变类型
data_03[-2] = "Kubernetes"

print(data_03)


# -------------------- 列表对象的操作方法 ----------------------------

# 1、append(), 追加数据
data_08 = [ "http" ]

data_08.append("https")
data_08.append("DNS")
data_08.append("DHCP")
data_08.append("FTP")

print(data_08)


# -------------------- 遍历列表 ----------------------------
apps = [ "nginx", "ftp", "php" ]

for i in apps:
    print("yum install -y %s" % i)

# -------------------- 遍历字符串 ----------------------------
test = "Linux"

for i in test:
    print(i)


# -------------------- 遍历列表 ----------------------------
# ssh 用户名@服务器IP -p 端口

servers = [ ["10.1.1.1", "admin", 22], ["10.1.1.2", "root", 44444] ]

for ip, user, port in servers:
    print("ssh %s@%s -p %s" % (user, ip, port))
