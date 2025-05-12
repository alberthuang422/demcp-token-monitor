# 使用 Python 3.13 作为基础镜像（根据 pyproject.toml 的要求）
FROM python:3.13-slim

# 设置工作目录
WORKDIR /app

# 安装 uv
RUN pip install uv

# 复制项目文件
COPY pyproject.toml .
COPY src/ ./src/

# 使用 uv 安装依赖
RUN uv pip install --system .


# 暴露端口
EXPOSE 8080

# 运行应用
CMD ["python", "src/token_monitor.py"] 