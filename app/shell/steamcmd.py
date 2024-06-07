import subprocess

# 设置steamcmd的路径
steamcmd_path = "D:\\steamcmd\\steamcmd.exe"

# 要下载的游戏的AppID
app_id = 322330

# 要保存游戏的目录
game_dir = "D:\\.klei"

# 构建steamcmd命令
command = [
    steamcmd_path,
    "+login", "anonymous",  # 使用匿名登录
    "+force_install_dir", game_dir,  # 设置安装目录
    "+app_update", str(app_id),  # 更新指定AppID的游戏
    "validate",  # 验证游戏文件
    "+quit"  # 退出steamcmd
]

# 运行steamcmd命令
try:
    # 使用subprocess.run来执行命令
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 打印输出结果
    print("stdout:", result.stdout.decode())
    print("stderr:", result.stderr.decode())
    print("Game download completed successfully.")
except subprocess.CalledProcessError as e:
    # 如果命令执行失败，打印错误信息
    print("SteamCMD encountered an error:", e.stderr.decode())