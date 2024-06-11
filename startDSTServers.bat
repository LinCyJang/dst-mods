@echo off
  cd /D "D:\.klei\bin64"
  start dontstarve_dedicated_server_nullrenderer_x64 -console -cluster MyDediServer -shard Master
  start dontstarve_dedicated_server_nullrenderer_x64 -console -cluster MyDediServer -shard Caves
  