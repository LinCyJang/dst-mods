import os
import requests
from zipfile import ZipFile
import subprocess
import platform
from app.utils.dir_path import get_file_root_path
# from steam import steam_client, steam_user, steam_webapi

steamcmd_url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'

target_folder = 'D:\\steamcmd'

if not os.path.exists(target_folder):
  os.makedirs(target_folder)

def get_cwd():
  system = platform.system()
  if system == 'Windows':
    return get_file_root_path() + '\steamcmd'
  else:
    return os.path.sep + 'steamcmd'
def download_file(url, folder):
    if not os.path.exists(folder):
      os.makedirs(folder)
    response = requests.get(url=url)
    if response.status_code == 200:
      with open(os.path.join(folder, 'steamcmd.zip'), 'wb') as f:
        f.write(response.content)
      return True
    else:
      print('下载失败！')
      return False
    
def extract_zip(path, to):
    print(path)
    try:
      with ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(to)
      return True
    except PermissionError as e:
      print(f"没有权限访问文件: {e}")
      return False


def run_steamcmd(steamcmd_folder):
    os.chdir(steamcmd_folder)
    commands = [
      'steamcmd.exe',
      "+login", "anonymous",  # 使用匿名登录
      "+app_update", str(343050),  # 更新指定AppID的游戏
      "validate",  # 验证游戏文件
      "+quit"  # 退出steamcmd
    ]
    try:
      print('开始下载游戏')
      with subprocess.Popen(commands,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
        print('正在下载中，文件比较大，需要的时间比较长...')
        stdout, stderr = proc.communicate()
        print('运行日志：')
        print(stdout)
      
      if stderr:
        print('错误日志')
        print(stderr)
      output = {
        'stdout': stdout,
        'stderr': stderr,
      }
      return output
    except FileNotFoundError as F:
      print(f'错误：{F}')
      return False

# 创建存档
def create_base_file():
  dir_name = ' MyDedServer'
  if not os.path.exists(dir_name):
      os.makedirs(dir_name)
    
  sub_dirs = ['Master', 'Caves']
  for sub_dir in sub_dirs:
     full_path = os.path.join(dir_name, sub_dir)
     if not os.path.exists(full_path):
        os.makedirs(full_path) 

  config_files = [
     'cluster.ini',
      'cluster_token.txt',
      'Master/server.ini',
      'Master/modoverrides.lua',
      'Master/worldgenoverride.lua',
      'Caves/server.ini',
      'Caves/modoverrides.lua',
      'Caves/worldgenoverride.lua'
  ]

  for config_file in config_files:
     full_path = os.path.join(dir_name, config_file)


def create_start_bat():
  print('bat脚本')
  # 定义要写入的BAT脚本内容
  bat_script_content = """@echo off
  cd /D "D:\\.klei\\bin64"
  start dontstarve_dedicated_server_nullrenderer_x64 -console -cluster MyDediServer -shard Master
  start dontstarve_dedicated_server_nullrenderer_x64 -console -cluster MyDediServer -shard Caves
  """

  # 文件路径
  file_path = 'startDSTServers.bat'

  # 打开文件并写入内容
  with open(file_path, 'w') as file:
      file.write(bat_script_content)

  print(f'BAT脚本已保存到{file_path}')
    