# API_Space_for_your_stories

API_Space_for_your_stories —  это проект социальной сети, где пользователи могут публиковать свои истории, делиться отзывами и общаться друг с другом.

Социальная сеть позволяет:
- создавать учетную запись;
- авторизированным пользователям публиковать посты, осуществлять подписку на авторов, оставлять комментарии к посту;
- авторам удалять или редактировать свои посты или комментарии;
- просмотр информации о посте или комментарии неавторизированным пользователям.
  
Данный интерфейс позволяет осуществлять передачу данных в формате JSON в любое приложение или на фронтенд, что дает возможность организовать работу мобильного приложения или чат-бот.

### Технологии
[![Python](https://img.shields.io/badge/-Python3.9-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2.16-blue?logo=django)](https://www.djangoproject.com/)
[![Django](https://img.shields.io/badge/django--rest--framework-3.12.4-blue?)](https://www.django-rest-framework.org/)
[![Django](https://img.shields.io/badge/Simple_JWT-5.2.2-blue?)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
[![Django](https://img.shields.io/badge/Djoser-2.2.0-blue?)](https://djoser.readthedocs.io/en/latest/)


### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Tatiana314/API_Space_for_your_stories.git && cd API_Space_for_your_stories 
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
Linux/macOS: source env/bin/activate
windows: source env/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
В директории API_Space_for_your_stories создать и заполнить файл .env:
```
touch .env

SECRET_KEY='Секретный ключ'
ALLOWED_HOSTS='Имя или IP хоста'
DEBUG=True
```
Выполнить миграции и запустить проект:
```
python yatube_api/manage.py migrate && python yatube_api/manage.py runserver
```

Документация для API доступна по адресу http://127.0.0.1:8000/redoc/. 
Документация представлена в формате Redoc.

### Пример:
```
GET запрос http://127.0.0.1:8000/api/v1/posts/
```
<img width="364" alt="код" src="https://github.com/Tatiana314/api_final_yatube/assets/124789269/52ce389b-04dd-4ef6-b4ea-3953e2a540ef">

## Автор
[Мусатова Татьяна](https://github.com/Tatiana314)
