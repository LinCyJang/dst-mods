# -*- coding: utf-8 -*-

from flask import Flask
from app.routes.mods_routes import mods_routes
from app.json_flask import JsonFlask

def create_app():
  app = JsonFlask(__name__)
  app.register_blueprint(mods_routes, url_prefix='/dst/v1')
  
  return app