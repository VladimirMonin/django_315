from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Представление для главной страницы.
    """
    return HttpResponse(
        """<h1>Мой блог!</h1>
        <a href="/category/">Категории</a>
        """
    )  # вернет страничку с заголовком "Мой блог!" на русском языке.


def category(request):
    """
    Представление для категорий.
    """
    return HttpResponse(
        """<ul><li>Python</li><li>Django</li><li>Flask</li></ul>
        <a href="/">На главную</a>
        """
    )  # вернет список категорий на русском языке.
