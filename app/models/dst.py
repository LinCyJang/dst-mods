# -*- coding: utf-8 -*-


import subprocess

# 启动终端会话
process = subprocess.Popen("dir", shell=True)

if process.returncode == 0:
  output, error = process.communicate()
  print(output.decode('gbk'))
  print('success')
else:
  print('error')

