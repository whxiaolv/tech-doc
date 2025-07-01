# 使用官方 Nginx 基础镜像
#FROM nginx:alpine

# 安装 tini , 使用 nginx:latest
FROM nginx:latest
RUN apt-get update && apt-get install -y tini

# 删除默认的 Nginx 欢迎页面
RUN rm -rf /usr/share/nginx/html/*
COPY . .
# 暴露 80 端口
EXPOSE 80
# 启动 Nginx 服务
CMD ["nginx", "-g", "daemon off;"]