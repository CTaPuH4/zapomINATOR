# запомИНАТОР

## Помошник в учёбе на базе искуственного интелекта
API, создающее карточки с вопросами по загруженному тексту в форматах .txt, .pdf или .docx на базе искуственного интелекта.

## Запуск проекта
Клонировать репозиторий и перейти в него в командной строке.

Активировать виртуальное окружение:
```
python -m venv venv
. venv/Scripts/activate
```

Установить сторонние библиотеки:
```
pip install -r requirements.txt
```

Запустить миграции:
```
python manage.py migrate
```

Запустить проект:
```
python manage.py runserver
```

## Примеры запросов
- localhost:8000/files/ - **POST** - загрузка файла
- localhost:8000/cards/ - **GET** - получение карточек
- loacalhost:8000/cards/clear/ - **POST** - удаление всех карточек

### Авторы
Nizhelskiy Ilya (CTaPuH4) - https://github.com/CTaPuH4