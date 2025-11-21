from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import *

def index(request):
    orders = Orders.objects.all()
    return render(request, 'index.html', {'orders': orders})

def create_order(request):
    if request.method == "POST":
        surname = request.POST.get("surname")
        if not surname:
            return HttpResponseNotFound("<h2>Фамилия не указана</h2>")

        order = Orders.objects.create(surname=surname)
        for book_id in request.POST.getlist("books"):
            OrderedBooks.objects.create(order=order, book_id=book_id, quantity=1)
        return HttpResponseRedirect("/")

    books = Books.objects.all()
    return render(request, "create_order.html", {"books": books})


