import shutil
import os


def fileReplace():
    src_file = r"D:\python\fileTest\test2.txt"
    # 创建临时文件
    tmp_file = r"D:\python\fileTest\test2_tmp.txt"
    tmp_obj = open(tmp_file, mode="w")

    with open(src_file, mode="r") as src_obj:
        for line in src_obj:
            if "shell" in line:
                new_line = line.replace("shell", "python")
                tmp_obj.write(new_line)
            else:
                tmp_obj.write(line)

    tmp_obj.close()

    shutil.copy(tmp_file, src_file)
    os.remove(tmp_file)

if __name__ == '__main__':
    fileReplace()
