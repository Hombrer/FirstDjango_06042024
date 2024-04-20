from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity": 5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity": 12},
   {"id": 7, "name": "Картофель фри" ,"quantity": 0},
   {"id": 8, "name": "Кепка" ,"quantity": 124}
]


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.com"
    }
    return render(request, "index.html", context)


def about(request):
    result = f"""
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(result)


# url -> item/1
# url -> item/2
# ...
# url -> item/n
def get_item(request, item_id: int):
    for item in items:
        if item["id"] == item_id:
            response = f"""
            <h2>Название: {item['name']}</h2>
            <p>Количество: {item['quantity']}</p>
            <p><a href="/items"> Назад к списку товаров </a></p>
            """
            return HttpResponse(response)
    return HttpResponseNotFound(f'Товар с id={item_id} не найден')


# <ol>
#    <li> ... </li>
#    <li> ... </li>
#    <li> ... </li>
# </ol>
def items_list(request):
    # response = "<h1> Список товаров </h1><ol>"
    # for item in items:
    #     response += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # response += "</ol>"
    # return HttpResponse(response)
    context = {
        "items": items,
    }
    return render(request, "items_list.html", context)