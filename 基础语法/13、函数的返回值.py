'''
函数的返回值：
    return  数据

    注意：return是函数的终止
'''

def sum(a, b):
    data = a + b
    return data

if __name__ == '__main__':
    # 接收函数返回的数据
    result = sum(10, 20)
    if result > 100:
        print("OK")
    else:
        print("not OK")