from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

CATEGORIES = {
    1: "Чилл территории Python",
    2: "Django, сложно, но можно!",
    3: "Flask, бегите, глупцы!",
}


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
