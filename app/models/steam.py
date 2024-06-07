import os
import requests
from zipfile import ZipFile
from io import BytesIO
import subprocess
# from steam import steam_client, steam_user, steam_webapi

steamcmd_url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'

target_folder = 'D:\\steamcmd'

if not os.path.exists(target_folder):
  os.makedirs(target_folder)
  
def download_file(url, folder):
    response = requests.get(url=url)
    if response.status_code == 200:
      with open(os.path.join(folder, 'steamcmd.zip'), 'wb') as f:
        f.write(response.content)
        return True
    else:
      print('下载失败！')
      return False
    
def extract_zip(path, to):
    with ZipFile(path, 'r') as zip_ref:
      zip_ref.extractall(to)


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
    except FileNotFoundError as F:
      print(f'错误：{F}')
    except Exception as e:
      print(f'错误：{e}')
# def login_steam(username, passwrod, target_folder):
#     client = stea

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
    
    

def test():
    if download_file(steamcmd_url, target_folder):
      print('下载成功！')
      
      zip_path = os.path.join(target_folder, 'steamcmd.zip')
      if not os.path.isfile(os.path.join(target_folder, 'steamcmd.exe')):
        print("steamcmd.zip needs to be extracted.")
        extract_zip(zip_path, target_folder)
        print('解压成功')
      
      run_steamcmd('D:\\steamcmd')
      print('安装成功')
      
# test()
create_start_bat()
