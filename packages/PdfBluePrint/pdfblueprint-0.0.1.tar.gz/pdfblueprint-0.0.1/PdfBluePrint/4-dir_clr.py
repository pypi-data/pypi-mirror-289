import os
import shutil
import glob

##def delete_files_with_extension(directory, extension):
##    file_list = glob.glob(os.path.join(directory, f'*.{extension}'))
##    for file_path in file_list:
##        os.remove(file_path)


## 如果连目录本身一起删除的话
##def delete_files(directory):
##    shutil.rmtree(directory)

def delete_files(directory):
    file_list = os.listdir(directory)
    for file in file_list:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

# 调用示例
directory_path_list = ['./images','./pdfs','./output']
for directory_path in directory_path_list:
    delete_files(directory_path)

