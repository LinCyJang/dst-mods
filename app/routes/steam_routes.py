from flask import Blueprint, request
from app.models.system import get_system
from app.json_response import JsonResponse
import os
import platform
from app.models.steam import download_file, extract_zip, run_steamcmd
from app.utils.dir_path import get_file_root_path

steam_route = Blueprint('steam_routes', __name__)

@steam_route.route('install-steamcmd', methods=['GET'])
def install_steamcmd_route():
    system = platform.system()
    if system == 'Windows':
      target_folder = get_file_root_path() + 'steamcmd'
    else:
      target_folder = os.path.sep + 'steamcmd'
    steamcmd_url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'
    steamcmd_file = download_file(steamcmd_url, target_folder)
    zip_path = os.path.join(target_folder, 'steamcmd.zip')
    if steamcmd_file:
      success = extract_zip(zip_path, target_folder)
      if success:
        return JsonResponse.success(data={"path": target_folder}, msg='steamcmd安装成功')
      else: 
        return JsonResponse.error(data=[],msg='steamcmd安装失败')
    else:
      return JsonResponse.error(data=[],msg='steamcmd下载失败')

@steam_route.route('install-dst-server', methods=['GET'])
def install_dst():
    print('')
    path = request.args.get('path')
    log = run_steamcmd(path)
    if log:
      return JsonResponse.success(data=log, msg='DST安装成功')
    else:
      return JsonResponse.error(data=[],msg='DST安装失败')
      
    
@steam_route.route('system', methods=['GET'])
def get_system_route():
    system = get_system
    if system:
      return JsonResponse.success(data=system)
    else:
      return JsonResponse.error(data=[])