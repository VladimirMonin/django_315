## Lesson 49

### Получаем Ракету Django!

1. Установка Django:
```bash
pip install django
```

2. Создание нового проекта в Django:
   
```bash
django-admin startproject blog .
```

Вариант с точкой создаст новый проект в текущей директории, а вариант без точки создаст новую директорию с именем проекта.

1. Запуск сервера разработки:
```bash
python manage.py runserver
```

4. Создание нового приложения в проекте:
```bash
python manage.py startapp python_blog
```

**lesson_49: Создание проекта Blog и приложения python_blog**

### INSTALLED_APPS

1. Добавили приложение в `INSTALLED_APPS` в файле `settings.py`:
2. Добавили функцию index в файле `views.py` в приложении `python_blog`
3. Импортировали функцию index в файле `urls.py` в приложении `python_blog`
4. Добавили путь к функции index в файле `urls.py` в приложении `python_blog`


`INSTALLED_APPS` - это список всех приложений, установленных в Django. При создании нового приложения, его необходимо добавить в `INSTALLED_APPS` в файле `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'python_blog',
]
```

**lesson_49: Создание первого представления с HTTP-ответом**

### Представление `/category/`

1. Добавили функцию `category` в файле `views.py` в приложении `python_blog`
2. Импортировали функцию `category` в файле `urls.py` в приложении `python_blog`
3. Добавили путь к функции `category` в файле `urls.py` в приложении `python_blog`
4. Добавили ссылки на обоих страницах для перехода между ними

В этот раз мы использовали в строке ответа полноценный HTML код, который будет отображаться в браузере.

```html
<ul><li>Python</li><li>Django</li><li>Flask</li></ul>
        <a href="/">На главную</a>
```

**lesson_49: Представление категорий**


### `include` в `urls.py`

1. Создали собственный файл `urls.py` в приложении `python_blog`
2. Подключили файл `urls.py` из приложения `python_blog` в файле `urls.py` в конфигурационном пакете с префиксом `/blog/`
3. Протестировали работу приложения
4. Создали конфигурацию запуска сервера разработки в PyCharm / VSCode


`include` - это функция, которая позволяет подключить файл `urls.py` из приложения в файл `urls.py` в конфигурационном пакете. 


**lesson_49: Пакетное подключение маршрутов через include**