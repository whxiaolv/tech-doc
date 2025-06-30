# 使用官方 Nginx 基础镜像
FROM nginx:alpine
# 删除默认的 Nginx 欢迎页面
RUN rm -rf /usr/share/nginx/html/*
# 复制当前目录下的内容到 Nginx 默认网站目录
COPY . /usr/share/nginx/html
# 复制脚本文件
COPY ./test.sh ./test.sh
# 执行
RUN chmod +x /test.sh
# 暴露 80 端口
EXPOSE 80
# 启动 Nginx 服务
CMD ["nginx", "-g", "daemon off;"]