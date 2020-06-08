# Docker Compose

Инструмент для создания и запуска многоконтейнерных Docker приложений. В Compose, вы используете специальный файл для конфигурирования ваших сервисов приложения. Затем, используется простая команда, для создания и запуска всех сервисов из конфигурационного файла. Самая тривиальная реализация микросервисной архитектуры

Использование Compose обычно разделяется на три этапа:

1. Определение окружения вашего приложения в Dockerfile, это можно сделать в любом месте;

2. Определение сервисов из которых будет состоять ваше приложение в docker-compose.yml, в последствии они смогут быть запущены все вместе в изолированном окружении;

3. И наконец, выполнение команды docker-compose up которая запустит все ваше приложение.

## Пример

>  Создание проекта 

Нужно создать:
1. Файл docker-compose.yml;
2. Папку server (здесь будут файлы сервера);
3. Папку client (здесь будут файлы клиента). 

> Сервер

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

> Клиент

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

> Docker Compose





