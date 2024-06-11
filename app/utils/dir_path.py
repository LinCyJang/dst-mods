import os
import platform


# 获取当前目录地址
def get_current_path(): 
    return os.getcwd()

#获取文件所在目录地址
def get_file_path():
  return os.path.dirname(os.path.abspath(__file__))

# 获取系统根目录地址
def get_root_path():
    system = platform.system()
    if system == 'Windows':
      return
    else:
      return os.path.sep

# 获取当前文件的根目录地址
def get_file_root_path():
    file_path = os.path.abspath(__file__)
    while not os.path.ismount(file_path):
      # 移动到上一级目录
      file_path = os.path.dirname(file_path)
    return file_path