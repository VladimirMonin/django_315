from calendar import c
from django.shortcuts import render
from django.http import Http404
from django.template import context

CATEGORIES = {
    1: "Чилл территории Python",
    2: "Django, сложно, но можно!",
    3: "Flask, бегите, глупцы!",
}

CATEGORIES_2 = [
    {
        'id': 1,
        'name': 'Python',
        'description': 'Чилл территории Python'
    },
    {
        'id': 2,
        'name': 'Django',
        'description': 'Django, сложно, но можно!'
    },
    {
        'id': 3,
        'name': 'Flask',
        'description': 'Flask, бегите, глупцы!'
    }
]

# page_alias - переменная, которая содержит алиас текущей страницы.
# Чтобы сделать её "активной"
# Нужно передать это значение через контекст в шаблон!!!

menu = [
    {
        "name": "Главная",
        "url": "/",
        "alias": "main"
    },
    {
        "name": "Блог",
        "url": "/blog/",
        "alias": "blog"
    },
    {
        "name": "О проекте",
        "url": "/about/",
        "alias": "about"
    }
]



def category_detail(request, category_id):
    """
    Представление для детальной страницы категории.
    blog/category/1/
    """
    category_id = int(category_id)
    category_str = CATEGORIES.get(category_id)
    context = {'message': category_str}
    if not category_str:
        raise Http404(f"Категория с id={category_id} не найдена")
    return render(request, 'python_blog/test_template.html', context=context)


def main(request):
    """
    Представление для главной страницы.
    """
    context = {"menu": menu}
    context['title'] = "Главная страница"
    context['page_alias'] = 'main'
    print(context)

    return render(request, 'main.html', context)


def about(request):
    """
    Представление для главной страницы.
    """
    context = {"menu": menu}
    context['title'] = "О нас"
    context['page_alias'] = 'about'

    return render(request, 'python_blog/about.html', context)


def blog(request):
    """
    Представление для главной страницы.
    """
    context = {"menu": menu}
    context['title'] = "Блог"
    context['page_alias'] = 'blog'

    return render(request, 'python_blog/blog.html', context)

def category(request):
    """
    Представление для категорий.
    #TODO - хорошее место для изучения циклов шаблонизатора.
    """
    context = {"categories": CATEGORIES_2}
    return render(request, 'python_blog/categoris_list.html', context)

