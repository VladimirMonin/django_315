from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

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
    #TODO - хорошее место для изучения циклов шаблонизатора.
    """
    context = {"categories": CATEGORIES_2}
    return render(request, 'python_blog/categoris_list.html', context)

class Developer:
    def __init__(self, name, stack:list):
        self.name = name
        self.stack = stack

    def __str__(self):
        return f"{self.name} - {self.stack}"
    
    def get_rus_info(self):
        return f"Разработчик {self.name} - {', '.join(self.stack)}"

about_data = {
    "title": "О нас",
    "text": "Мы - команда разработчиков, которая создает сайты на Django и Flask.",
    'stack_list': ['Python', 'Django', 'Flask'],
    "developers": [
        {"name": "Иван",
         "age": 25,
         "stack": ["Python", "Django"],
         "is_active": True},
        {"name": "Анна",
         "age": 23,
         "stack": ["Python", "Flask"],
         "is_active": True},
        {"name": "Петр",
         "age": 30,
         "stack": ["JS", "React", "Vue"],
         "is_active": False},

    ]}



# Представление которое отрисует about.html
def about(request):
    return render(request, "python_blog/about.html", about_data)
