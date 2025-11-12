'''
函数：功能重用

一、定义函数的语法

def 函数名称():
    xxxxxxxxxxxxx
    xxxxxxxxxxxxx
    xxxxxxxxxxxxx
    xxxxxxxxxxxxx

二、调用函数

    函数名称()
'''

import random
import string

def randomString(number=30):
    str = ""
    chars = string.ascii_lowercase + string.digits

    for i in range(number):
        str += random.choice(chars)

    print(str)

if __name__ == '__main__':
    randomString(10)
    randomString(20)
    randomString(60)
    randomString()


