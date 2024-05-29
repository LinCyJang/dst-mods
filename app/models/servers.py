import requests
from app.config import Config
import json



def get_lobby_regions(): 
    url = f'https://lobby-v2-cdn.klei.com/regioncapabilities-v2.json'
    response = requests.get(url)
    lobby_regions = []
    if response.status_code == 200:
        lobby_regions = response.json()
    else:
        print(f"Failed to retrieve projects. Status code: {response.status_code}")
    return lobby_regions

def get_lobby_serves(region='ap-east-1', platform='Steam'):
    url = f'https://lobby-v2-cdn.klei.com/{region}-{platform}.json.gz'
    response = requests.get(url)
    servers = []
    if response.status_code == 200:
        servers = response.json()
    else:
        print(f"Failed to retrieve projects. Status code: {response.status_code}")
    return servers

def get_server_info(region='ap-east-1', rowId=''):
    url = f'https://lobby-v2-{region}.klei.com/lobby/read'
    params = {
        "__token": "pds-g^KU_qE7e8rv1^VVrVXd/01kBDicd7UO5LeL+uYZH1+geZlrutzItvOaw=",
        "__gameId": "DST",
        "query": {
            "__rowId": rowId
        }
    }
    response = requests.post(url, data=json.dumps(params))
    info = {}
    if response.status_code == 200:
        info = response.json()
    else:
        print(f"Failed to retrieve projects. Status code: {response.status_code}")
    return info


# 发送 GET 请求到 Steam Web API 获取服务器列表
def get_servers():
    url = f'https://api.steampowered.com/IGameServersService/GetServerList/v1/'
    params = {
        'key': Config.STEAM_API_KEY,
        "filter": "\\appid\\322330",
    }

    response = requests.get(url, params=params)
    server_list = {}
    if response.status_code == 200:
        server_list = response.json()['response']
    else:
        print(f"Failed to retrieve projects. Status code: {response.status_code}")
    return server_list



