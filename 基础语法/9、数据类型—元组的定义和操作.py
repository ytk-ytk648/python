# 元组定义：定义在一对圆括号()中的数据, ( 元素, 元素, 元素 )
# 支持存储任意类型数据
# 核心不同：列表是可变， 元组是不可变

data_01 = ( 1, 2, 3, 4, 5 )
data_02 = ( "docker", "k8s", "harbor" )
data_03 = ( ["docker", "26.1"], ["k8s", "1.29"] )
data_04 = ( ("admin", "123"), ("martin", "redhat") )

print(type(data_01), type(data_02), type(data_03), type(data_04))

# 单元素的元组
data_05 = ( "nginx", )
print(type(data_05))

# 元组是不可变的
data_02 = ( "docker", "k8s", "harbor" )
print(data_02[-1])

data_03 = ( ["docker", "26.1"], ["k8s", "1.29"] )

data_03[-1][-1] = "1.32"

print(data_03)
