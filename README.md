###### 环境
    python 3.9.12

###### 本地运行

```
 git clone https://github.com/LinCyJang/dst-mods.git
```

```
cd ./dst-mods
```


```
pip install -r requirements.txt
```


```
python3 run.py
```


###### docker 运行


```
docker build -t dst-mods-app .
```


```
docker run -p 5000:5000 dst-mods-app
```
