# -*- coding: utf-8 -*-

from flask import Blueprint, request
from app.models.servers import get_servers,get_lobby_regions,get_lobby_serves,get_server_info
from app.json_response import JsonResponse

servers_route = Blueprint('servers_routes', __name__)

@servers_route.route('servers', methods=['GET'])
def get_servers_route():
    servers = get_servers()
    if servers:
      return JsonResponse.success(data=servers)
    else:
      return JsonResponse.error(data=[])

@servers_route.route('lobby-regions', methods=['GET'])
def get_lobby_regions_route():
    regions = get_lobby_regions()
    if regions:
      return JsonResponse.success(data=regions)
    else:
      return JsonResponse.error(data=[])

@servers_route.route('lobby-servers', methods=['GET'])
def get_lobby_servers_route():
    region = request.args.get('region')
    platform = request.args.get('platform')
    servers = get_lobby_serves(region=region, platform=platform)
    if servers:
      return JsonResponse.success(data=servers)
    else:
      return JsonResponse.error(data=[])

@servers_route.route('lobby-read', methods=['GET'])
def get_server_info_route():
  region = request.args.get('region')
  rowId = request.args.get('rowId')
  info = get_server_info(region=region, rowId=rowId)
  if info:
      return JsonResponse.success(data=info)
  else:
      return JsonResponse.error(data=[])