from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .models import *


def index(request):
    books = Books.objects.all()
    orders = Orders.objects.all()
    return render(request, 'index.html', {'books': books, 'orders': orders,})


def edit(request, id):
    try:
        book = Books.objects.get(id=id)
        if request.method == "POST":
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.price = request.POST.get("price")
            book.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"book": book})
    except Books.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")


def delete(request, id):
    try:
        book = Books.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/")
    except Books.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")


def create(request):
    if request.method == "POST":
        book = Books()
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.price = request.POST.get("price")
        book.save()
        return HttpResponseRedirect("/")
    books = Books.objects.all()
    return render(request, "create.html", {"books": books})


