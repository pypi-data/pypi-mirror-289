import os
import shutil
import glob

# 如果目录存在，则删除该目录及其所有内容
def delete_files(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"4 - Dir {directory} is now deleted.")
    else:
        print(f"4 - Dir {directory} NOT existed, skipped.")

# 要删除的目录列表
directory_path_list = ['./img_in', './img_out']

# 遍历目录列表，调用delete_files函数
for directory_path in directory_path_list:
    delete_files(directory_path)