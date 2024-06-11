# -*- coding: utf-8 -*-

from flask import Flask
from app.routes.mods_routes import mods_routes
from app.routes.servers_route import servers_route
from app.routes.system_routes import system_routes
from app.routes.steam_routes import steam_route
from app.json_flask import JsonFlask

def create_app():
  app = JsonFlask(__name__)
  app.register_blueprint(mods_routes, url_prefix='/dst/v1')
  app.register_blueprint(servers_route, url_prefix='/dst/v1')
  app.register_blueprint(system_routes, url_prefix='/dst/v1')
  app.register_blueprint(steam_route, url_prefix='/dst/v1')
  
  return app