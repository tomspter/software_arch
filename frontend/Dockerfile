FROM node:16 AS build

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm config set registry https://registry.npmmirror.com&&npm install --no-proxy

COPY . .

RUN npm run build

FROM nginx:latest
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]