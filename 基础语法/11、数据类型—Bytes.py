# bytes 字节， 特殊的字符串
# 定义：只支持字母、数字、特殊字符，不支持汉字

# 直接定义：
data_01 = b"linux"
print(type(data_01))

# 类型转换， 字符串 ---> bytes
data_02 = "杨帅 Love 峰哥"
new_data_02 = data_02.encode("utf-8")
print(type(new_data_02))
print(new_data_02)

# 类型： bytes ----> 字符串

data_03 = b'\xe6\x9e\xa8\xe6\xb8\x85 Love \xe5\xb2\xb0\xe5\x91\xa5'

new_data_03 = data_03.decode("utf-8")

print(type(new_data_03))
print(new_data_03)


