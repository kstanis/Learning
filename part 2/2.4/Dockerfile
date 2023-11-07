# Используем базовый образ Ubuntu 20.04
FROM ubuntu:20.04

# Устанавливаем необходимые компоненты и зависимости
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

# Устанавливаем Flask с помощью pip
RUN pip3 install Flask

# Создаем директорию внутри контейнера и копируем файлы веб-приложения
WORKDIR /app
COPY . /app

# Указываем порт, который будет использоваться в контейнере
EXPOSE 5000

# Указываем команду для запуска вашего веб-приложения
CMD ["python3", "app.py"]
