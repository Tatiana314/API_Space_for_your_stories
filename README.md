# REST API для социальной сети.

Социальная сеть позволяет:
- создавать учетную запись;
- авторизированным пользователям публиковать посты, осуществлять подписку на авторов, оставлять комментарии к посту;
- авторам удалять или редактировать свои посты или комментарии;
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

### Пример:
```
GET запрос http://127.0.0.1:8000/api/v1/posts/
```
<img width="364" alt="код" src="https://github.com/Tatiana314/api_final_yatube/assets/124789269/52ce389b-04dd-4ef6-b4ea-3953e2a540ef">


