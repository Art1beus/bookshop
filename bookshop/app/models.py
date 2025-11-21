from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    price = models.IntegerField()

class Orders(models.Model):
    date = models.CharField(max_length=30)
    surname = models.CharField(max_length=100)
    books = models.ManyToManyField(Books, through='OrderedBooks')


class OrderedBooks(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField()
