# Куда пойти

Сайт о самых интересных местах в Москве.

## Демо сайта

Демо сайта доступно по ссылке: https://paszhukov.pythonanywhere.com/

Чтобы добавлять и редактировать локации, используйте админку: https://paszhukov.pythonanywhere.com/admin/

Нижеследующие инструкции описывают, как развернуть проект на локальной машине.

## Установка зависимостей
Первым делом, скачайте код:
``` 
git clone https://github.com/pas-zhukov/yandex-afisha.git
```
Установите необходимые зависимости командой:
```
pip install -r requirements.txt
```

## Переменные окружения

Для работы проекта, в корень необходимо положить файл `.env` со следующими полями:

- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`. По умолчанию - `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`. <b>Обязательное поле!</b>
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `TIME_ZONE` — временная зона в общепринятом формате.


## Запуск

1. Применяем миграции
```shell
python manage.py migrate
```

2. Создаём суперпользователя

```shell
python manage.py createsuperuser
```

3. Запускаем dev сервер
```shell
python manage.py runserver
```

4. Открываем сайт по ссылке [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

5. Для редактирования локаций используем панель админа по адресу http://127.0.0.1:8000/admin/. Для входа используем данные созданного ранее суперпользователя. 

## Автоматизация загрузки локаций

Для автоматизации загрузки локаций предусмотрена специальная команда:
```shell
python manage.py load_place <URL или путь к json-файлу>
```

Json-файл локации должен иметь правильную структуру: [пример](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%20%D0%9C%D0%B0%D1%80%D0%BA%D1%81%D0%B0%20%D0%B8%D0%BB%D0%B8%20%C2%AB%D0%9A%D0%B0%D1%82%D1%83%D1%88%D0%BA%D0%B0%20%D0%A2%D0%B5%D1%81%D0%BB%D0%B0%C2%BB.json).

## Загрузка тестовых данных

1. Для загрузки тестовых данных скачайте папку `places` из [данного репозитория](https://github.com/devmanorg/where-to-go-places).

2. Создайте bash скрипт со следующим содержимым и запустите его:

```bash
#!/bin/bash
for file in <путь к папке places>/*
do
if [ -f "$file" ]
then
python <путь к папке с проектом>/manage.py load_place "$file"
fi
done
```

3. Если не было выведено ошибок, данные загружены в БД!

## Цели проекта

Код написан в учебных целях. Данные локаций взяты с сайта KudaGo.