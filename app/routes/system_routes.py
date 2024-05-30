# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify
from app.models.system import get_dir,get_newwork,get_system,get_cpu
from app.json_response import JsonResponse

system_routes = Blueprint('system_routes', __name__)

@system_routes.route('system', methods=['GET'])
def get_system_route():
  system_info = {
    "system": get_system(),
    "dir": get_dir(),
    "newwork": get_newwork(),
    "cpu": get_cpu()
  }
  return JsonResponse.success(data=system_info)
  