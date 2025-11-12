'''
hashlib模块 ：
    作用：对文件内容做md5校验
'''

import  hashlib

m = hashlib.md5()

with open(r"D:\python\fileTest\access_log", mode="rb") as fobj:
    content = fobj.read()
    m.update(content)

    print(m.hexdigest())

