FROM golang

ARG app_env
ENV APP_ENV $app_env


COPY . /go/server
WORKDIR /go/server

RUN go build

EXPOSE 8080