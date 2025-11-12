# --------- 获取命令的执行结果 ---------------
import os
result = os.popen("ping 10.11.0.254")
print(result)
print(result.read())
print(type(result.read()))


print("-------------" * 8)

# --------- 获取命令的执行状态码 ---------------
import subprocess
result = subprocess.call("ping 10.11.0.254", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("结果: ", result)
