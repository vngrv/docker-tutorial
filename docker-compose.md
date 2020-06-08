# Docker Compose

Инструмент для создания и запуска многоконтейнерных Docker приложений. В Compose, вы используете специальный файл для конфигурирования ваших сервисов приложения. Затем, используется простая команда, для создания и запуска всех сервисов из конфигурационного файла. Самая тривиальная реализация микросервисной архитектуры

Использование Compose обычно разделяется на три этапа:

1. Определение окружения вашего приложения в Dockerfile, это можно сделать в любом месте;

2. Определение сервисов из которых будет состоять ваше приложение в docker-compose.yml, в последствии они смогут быть запущены все вместе в изолированном окружении;

3. И наконец, выполнение команды docker-compose up которая запустит все ваше приложение.

## Пример

###  Создание проекта 

Нужно создать:
1. Файл docker-compose.yml;
2. Папку server (здесь будут файлы сервера);
3. Папку client (здесь будут файлы клиента). 

#### Сервер

В папке __server__ создать файлы:
* server.py
* index.html
* Dockerfile

Server.py

```python
1 #!/usr/bin/env python3
2 import http.server
3 import socketserver
4
5 handler = http.server.SimpleHTTPRequestHandler
6
7 with socketserver.TCPServer(("", 1234), handler) as httpd:
8    httpd.serve_forever()
```

index.html

```html
1 Hello world!
```

Dockerfile
```yml
1 FROM python:latest
2
3 ADD server.py /server/
4 ADD index.html /server/
5
6 WORKDIR /server/
```

#### Клиент

В папке __client__ создать файлы:
* client.py
* Dockerfile

Client.py
```python
1 #!/usr/bin/env python3
2 import urllib.request
3
4 fp = urllib.request.urlopen("http://localhost:1234/")
5
6 encodedContent = fp.read()
7 decodedContent = encodedContent.decode("utf8")
8
9 print(decodedContent)
10
11 fp.close()
```

Dockerfile
```yml
1 FROM python:latest
2
3 ADD client.py /client/
4
5 WORKDIR /client/
```

#### Docker Compose

```yml 
1 version: "3"
2 services:
3     server:
4         build: server/
5         command: python ./server.py
6         ports:
7             - 1234:1234
8     client:
9         build: client/
10        command: python ./client.py
11        network_mode: host
12        depends_on:
13            - server
```

#### Пояснение
1. __1 строчка__ -  Файл docker-compose должен начинаться с тега версии. Используется 3 как самая свежая;
2. __2 строчка__ - docker-composer работает с сервисами, те 1 сервис = 1 контейнер. Сервисом может быть клиент, сервер, база данных, сторонние сервисы. Обязательно начинается с services;
3. __3/8 строчка__ - имя сервиса;
4. __4/9 строчка__ - ключевое слово "build" используется при создании образа. Соответственно нужно указывать путь к Dockerfile;
5. __5 строчка__ - команда, которую нужно запустить после создания образа для старта сервера;
6. __6 строчка__ - использование порта для хост машины, чтобы был метчинг в виртуальную машину
7. __7 строчка__ - network_mode нужен для описания сети. Конкртенее тут будет обращание к localhost
8. __8 строчка__ - depends_on указывает должен ли сервис, ждать когда будут готовы другие сервисы и, затем, запускается

### Building

```sh
$ docker-compose build 
```

### Start
```sh
$ docker-compose up
```

### Usage

После выполнения всех команд следует перейти в браузере по адресу __http://localhost:1234/__ и увидеть "Hello world!"


# Задачи

1. Изучить каким образом в docker-compose можно инициализировать базу данных:
2. Создать docker обертку для текущего проекта в рамках программы обучения
3. Предотставить рабочую сборку в github

Вопросы **[сюда](https://vk.com/veng8)**.


