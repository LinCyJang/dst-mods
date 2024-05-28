# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify
from app.models.mods import get_mods
from app.json_response import JsonResponse

mods_routes = Blueprint('mods_routes', __name__)

@mods_routes.route('mods', methods=['GET'])
def get_mods_route():
  page = request.args.get('page')
  numperpage = request.args.get('pageSize')
  search_text = request.args.get('searchText')
  mods = get_mods(page=page, numperpage=numperpage, search_text=search_text)
  
  if mods:
    return JsonResponse.success(data=mods)
  else:
    return JsonResponse.error(data=[])