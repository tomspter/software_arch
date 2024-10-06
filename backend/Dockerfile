FROM golang:1.22-alpine

WORKDIR /app

COPY go.mod go.sum ./
RUN go env -w GOPROXY=https://goproxy.cn,direct&&go mod download

COPY . .

RUN go build -o main .

EXPOSE 8080

CMD ["./main"]