# REST API для социальной сети.

Социальная сеть позволяет:
- создавать учетную запись;
- авторизированным пользователям публиковать посты, осуществлять подписку на авторов, оставлять комментарии к посту;
- удаление и редактирование поста или комментария автором.
- просмотр информации о посте или комментарии неавторизированным пользователям.
  
Данный интерфейс позволяет осуществлять передачу данных в формате JSON в любое приложение или на фронтенд, что дает возможность организовать работу мобильного приложения или чат-бот.

### Технологии
Python3, Django3, Django REST Framework

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Tatiana314/api_final_yatube.git
```
```
cd api_final_yatube 
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```

Документация для API доступна по адресу http://127.0.0.1:8000/redoc/ после запуска сервера разработчика. Документация представлена в формате Redoc.

### Примеры:
```
http://127.0.0.1:8000/api/v1/posts/
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
{
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
