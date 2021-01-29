# Вытаскиваем базовый образ
FROM python:3.8

# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Создаем папку(рабочий каталог)

RUN mkdir /code
# Настраиваем и переходим в рабочий каталог
# WORKDIR sets the working directory for all the command after it is defined in the Dockerfile, which means the command which you are try to run will run from that directory.
WORKDIR /code
# Устанавливаем зависимости
ADD requirements.txt /code/
RUN pip install -r requirements.txt

#RUN python manage.py migrate
# Копируем проект
COPY . /code/

CMD ["python3", "manage.py"]