FROM golang:1.22-alpine

# 设置工作目录
WORKDIR /app

# 将 go.mod 和 go.sum 复制到容器中，并下载依赖
COPY go.mod go.sum ./
RUN go env -w GOPROXY=https://goproxy.cn,direct&&go mod download

# 将源代码复制到容器中
COPY . .

# 编译 Go 应用
RUN go build -o main .

# 设置 Gin 服务器运行的端口
EXPOSE 8080

# 启动应用
CMD ["./main"]