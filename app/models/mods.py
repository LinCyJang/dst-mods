# -*- coding: utf-8 -*-

import requests
from app.config import Config
# '73DF9F781D195DFD3D19DED1CB72EEE6', 
def get_mods(page=1, numperpage=25, search_text=''):
    data = {
      'page': page,
      'key': Config.STEAM_API_KEY,
      'language':6,
      'appid': 322330,
      'return_tags': True,
      'numperpage': numperpage,
      'search_text': search_text,
      'return_vote_data': True,
      'return_children': True
    }
    response = requests.get(f'http://api.steampowered.com/IPublishedFileService/QueryFiles/v1/', params=data)
    mods = {}
    if response.status_code == 200:
        mods = response.json()['response']
    else:
      print(f"Failed to retrieve projects. Status code: {response.status_code}")
    return mods
