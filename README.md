# Django course

## Инструкция по развертыванию проекта

1. Создание виртуального окружения
```
python3 -m venv venv_name
```

2. Активация виртуального окружения
```
source venv_name/bin/activate
```

3. Установка пакетов в виртуальное окружение
```
pip install -r requirements.txt
```

4. Применение миграций
```
python manage.py migrate
```

5. Запуск сервера `django`
```
python manage.py runserver
```
## Запуск `ipython` в контексте приложений `django`
```
python manage.py shell_plus --ipython
```

## Загрузка и выгрузка данных из БД
### Выгрузить данные из БД
```
python manage.py dumpdata MainApp --indent 4 > MainApp/fixtures/save_all.json
```

### Загрузить данные в БД
```
python manage.py loaddata MainApp/fixtures/save_all.json
```

## Официальная документация 

[English](https://docs.djangoproject.com/en/5.0)  

[Русский](https://django.fun/docs/django/5.0)


