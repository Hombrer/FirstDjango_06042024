from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item



def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.com"
    }
    return render(request, "index.html", context)


def about(request):
    author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
    }
    result = f"""
    <header>
        / <a href="/"> Home </a> / <a href="/items"> Items </a> / <a href="/about"> About </a>
    </header>
    <br><br>
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(result)


def get_item(request, item_id: int):
    """ По указанному id возращаем имя элемента и его кол-во """
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Товар с id={item_id} не найден')
    else:
        context = {
            "item": item
        }
        return render(request, "item_page.html", context)
    

def items_list(request):
    """ Get all items from database """
    items = Item.objects.all()
    context = {
        "items": items,
    }
    return render(request, "items_list.html", context)