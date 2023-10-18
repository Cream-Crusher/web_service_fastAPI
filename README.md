# web_service_fastAPI

[Задание](https://drive.google.com/file/d/1-vHxd6eZzk5CBZDfeYI4yR_31Tz_V58C/view?usp=sharing)

API для парсинга вопросов викторин.

## Стэк
* Python 3.10
* docker + docker-compose
* FastAPI 0.103.1
* SQLAlchemy 2.0.20
* PostgreSQL 15.2
* Alembic 1.12.0

## Запуск

### Clone repo
```git clone git@github.com:Cream-Crusher/web_service_fastAPI.git```
### Run docker
A. Linux:
  1. ```docker-compose up --build```

B. Windows:
  1. Replace ```psycopg2-binary==2.9.7``` with ```psycopg2==2.9.7``` in **requirements.txt**
  2. ```docker-compose up --build```

### View Swagger
```http://0.0.0.0:8000/docs#```

## Особенности реализации
### Сущностные классы:
* Quiz - модель Задания для викторины (вопрос + правильный ответ + мета)
* Category - модель Категории для заданий викторины

### Сервисы:
* **question_service**
  * **get_questions**(questions_num: int) - выполняет запрос к стороннему сервису ```jservice.io/api/random```, возвращая json-ответ с ```questions_num``` случайными Заданиями викторин.
* **quiz_service**
  * **try_create_quiz**(session: AsyncSession, question: dict) - записывает в БД новое задание из json-объекта и возввращает ```TRUE```. Если Задание с таким ```id``` уже существует в БД, то добавления не происходит и возвращается ```FALSE```.
  * **try_get_prev_quiz**(session: AsyncSession) - возвращает предыдущую сохраненную запись Задания из БД, если записей в БД нет - ```NONE```.
* **category_service**
  * **get_or_create_category**(session: AsyncSession, category) - записывает в БД новую Категорию из json-объекта или возвращает существующую (совпадает ```id```).

### REST-API:
* [POST] **post_quiz**(questions_num: QuestionsNumDTO, session: AsyncSession = Depends(get_session)) - выполняет запросы к стороннему сервису до тех пор, пока не наберется ```questions_num``` новых уникальных Заданий и записывает их в БД. Возвращает предыдущую сохраненную запись.
  Пользуется сервисами, описанными выше.
