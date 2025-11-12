# 字典定义：被大括号{}括起来，数据格式为：{ key: value, key: value, key: value }
# 字典的 key 是唯一的，value可以是任意类型的数据
# 字典：可变的

data_01 = {}
data_02 = { "docker":"26.1", "k8s":"1.29" }
data_03 = {
    "192.168.1.1": {
        "user": "admin",
        "password": "123456"
    },
    "192.168.1.2": {
        "user": "martin",
        "password": "redhat"
    }
}

print(type(data_01), type(data_02), type(data_03))

# ------ 获取数据, 根据键获取数据----------
data_02 = { "docker":"26.1", "k8s":"1.29" }
print(data_02["docker"])

version = data_02.get("k8s")
print(version)

# ------ 添加数据, 根据键添加数据----------
# 字典名称[键] = 值
data_02 = { "docker":"26.1", "k8s":"1.29" }

data_02["prometheus"] = "3.7"

print(data_02)

# ------ 修改数据, 根据键修改数据----------
# 字典名称[键] = 值

data_02["k8s"] = "1.32"

print(data_02)


# ------------- 字典对象的操作方法 ---------------

# 1、keys() 以列表的形式获取字典中所有的键
data_02 = { "docker":"26.1", "k8s":"1.29", "promethues":"3.7" }
print(data_02.keys())
print("nginx" in data_02.keys())

# 2、items(), 获取字典中所有的键值对， 配合遍历字典用
print(data_02.items())

# ------------- 遍历字典 ---------------
# 软件名称: xxxxxx,   软件版本: xxxxxx

data_02 = { "docker":"26.1", "k8s":"1.29", "promethues":"3.7" }

for k, v in data_02.items():
    print("软件名称: %s, 软件版本: %s" % (k, v))


# ssh 用户名@服务器地址
data_03 = {
    "192.168.1.1": {
        "user": "admin",
        "password": "123456"
    },
    "192.168.1.2": {
        "user": "martin",
        "password": "redhat"
    }
}

for ip, info in data_03.items():
    print("ssh %s@%s" % (info.get("user"), ip))



test = {
           "jsonrpc": "2.0",
           "result": [
               {
                   "hostid": "10084",
                   "host": "Zabbix server",
                   "interfaces": [
                       {
                           "interfaceid": "1",
                           "ip": "127.0.0.1"
                       }
                   ]
               }
           ],
           "id": 2
       }

number = test.get("result")[0].get("interfaces")[0].get("interfaceid")

print(number)
