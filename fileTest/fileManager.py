import os
import datetime

# 获取任意目录下的文件路径
def get_file_path(directory):
    file_path_list = []
    for dir_name, sub_dir_list, file_list in os.walk(directory):
        # 判断当前目录下是否有文件
        if len(file_list) > 0:
            for f_name in file_list:
                file_path = dir_name + "\\" + f_name
                file_path_list.append(file_path)
    return file_path_list

# 重命名    a.txt ------ > a_YYYY_MM_DD.txt     a_时间.txt
def file_rename():
    file_path = get_file_path(r"D:\python\fileTest\北京")
    for src_file_name in file_path:
        # 获取文件的创建时间
        create_timestamp = os.path.getctime(src_file_name)
        create_time = datetime.datetime.fromtimestamp(create_timestamp).strftime("%Y_%m_%d")
        if create_time not in src_file_name:
            # 拼接新文件名
            prefix = src_file_name.split(".")[0]
            suffix = src_file_name.split(".")[1]
            new_file_name = prefix + "_" + create_time + "." + suffix
            os.rename(src_file_name, new_file_name)


if __name__ == '__main__':
    file_rename()
