@echo off
  cd /D "D:\steamcmd\steamapps\common\Don't Starve Together Dedicated Server\bin64"
  start dontstarve_dedicated_server_nullrenderer_x64 -console -cluster MyDediServer -shard Master
  start dontstarve_dedicated_server_nullrenderer_x64 -console -cluster MyDediServer -shard Caves
  