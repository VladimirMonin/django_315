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

### Знакомство с конвертерами путей
1. Добавили маршрут детального представления категории `category/<int:category_id>/` в файле `urls.py` в приложении `python_blog`
2. Добавили функцию `category_detail` в файле `views.py` в приложении `python_blog`


**lesson_49: конвертер путей для детального представления категорий**

### Http 404
1. Добавили в функцию `category_detail` обработку исключения `Http404`
Если категория не найдена, то будет возвращен ответ с кодом 404

**lesson_49: Обработка исключения Http404**

## Lesson 50

### Знакомство с шаблонами

1. Создали папку `templates` в приложении `python_blog`
2. В ней создали подпапку `python_blog` для того, чтобы шаблоны не пересекались с шаблонами других приложений
3. Создали `test_template.html` в папке `python_blog` и добавили в него код
4. В нем сделали переменную `{{ message }}`
5. Этот шаблон рендерит `category_detail` и передает туда переменную `message`

**lesson_50: Первый шаблон и передача переменной**


## Lesson 51 Переменные, теги, циклы в шаблонах Django

### Переменные в шаблонах

1. Посмотрели на синтаксис переменных `{{ variable }}` в шаблонах Django
2. Добавили `about.html` в маршруты в конфигурационном пакете `/about/`
3. Создали шаблон `about.html` и передали в него переменные:
   1. `title`
   2. `text`
   3. `stack_list` - список (можно добыть элемент циклом или по индексу)
   4. `developer1` - объект, можно добыть атрибуты объекта, или вызвать методы (без параметров!)


**lesson_51: Переменные в шаблонах Django**

### Цикл внутри цикла в шаблонах Django

1. Дополнили контекст с использованием списка словарей, где один из ключей содержит список.
2. В шаблоне `about.html` создали цикл внутри цикла для вывода всех элементов списка словарей.

```html
<li>
        <h3>{{ developer.name }}</h3>
        <p>Возраст: {{ developer.age }}</p>
        <p>Стек технологий:</p>
        <ul>
          {% for stack in developer.stack %}
          <li>{{ stack }}</li>
          {% endfor %}
        </ul>
      </li>
```


**lesson_51: Цикл внутри цикла в шаблонах Django**

### IF в шаблонах Django

1. Модфицировали дата-сет, добавив каждому разработчику ключ `is_active`
2. В шаблоне `about.html` добавили условие `if` для вывода информации о разработчике, если он активен.


**lesson_51: Условие IF в шаблонах Django**


### forloop - Объект цикла в шаблонах Django


| Атрибут               | Описание                                                                                  |
| --------------------- | ----------------------------------------------------------------------------------------- |
| `forloop.counter`     | Порядковый номер текущей итерации цикла, начиная с 1.                                     |
| `forloop.counter0`    | Порядковый номер текущей итерации цикла, начиная с 0.                                     |
| `forloop.revcounter`  | Количество оставшихся итераций цикла, включая текущую, начиная с общего числа элементов.  |
| `forloop.revcounter0` | Количество оставшихся итераций цикла, не включая текущую, начиная с общего числа минус 1. |
| `forloop.first`       | Возвращает `True`, если текущая итерация является первой.                                 |
| `forloop.last`        | Возвращает `True`, если текущая итерация является последней.                              |
| `forloop.parentloop`  | Для вложенных циклов, это ссылка на `forloop` внешнего цикла.                             |


1. Добавили условие в цикл, что если это последний сотрудник, делаем горизонтальную линию
2. Она не отрисовалась, потому что было условие что мы рисуем только активных сотрудников
3. Убрали это условие.
4. Все заработало.


**lesson_51: Объект цикла forloop в шаблонах Django**


### Тег шаблонов `url`

Этот тег использует псевдоним маршрута. Его надо задать в `urls.py`
Делается это через аргумент `name` в функции `path`

Сделали ссылку на страницу `about` через тег `url` в шаблоне `index.html`

```html
 <a href="{% url 'about' %}">About</a>
```


**lesson_51: Тег шаблонов url в Django**

### Передача аргументов в теге `url`

Для примера мы использовали числовой конвертер категорий.
Так же, нам пришлось модифицировать данные для контекста, чтобы иметь доступ к id и описанию категорий.

```python
   {
        'id': 1,
        'name': 'Python',
        'description': 'Чилл территории Python'
    }
```

**lesson_51: Передача аргументов в теге url в Django**

### Фильтры в шаблонах Django

Добавили в шаблон фильтр join для объединения элементов списка в строку через разделитель.

```html
<p>Попробуем отрисовать это циклом: {{ stack_list|join:" | " }}</p>
```

**lesson_51: Фильтры в шаблонах Django**


## Lesson 52 - Наследование шаблонов

1. Создали ветку `lesson_52_templates`
2. Создали в корневой директрии каталог с шаблонами `templates`
3. Прописали в `settings.py` путь к каталогу с шаблонами
4. Создали базовый шаблон `base.html` и добавили в него BS5, много блоков.
5. Сделали наследника `main.html` и добавили в него блоки `title` и `content`
6. Сделали в корневом `templates/includes` подпапку для включений.
7. Сделали `nav.html` и добавили его в `base.html` через тег `{% include %}`
8. Перенастроили вьюшку `main` на использование шаблона `main.html` на главной странице


**lesson_52: Главный шаблон, наследование и включения**