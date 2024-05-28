# 使用 Python 官方镜像作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装项目依赖
RUN pip install -r requirements.txt

# 暴露应用程序端口（如果需要）
EXPOSE 5000

# 启动应用程序
CMD ["python", "run.py"]
