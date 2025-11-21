from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=25)
    price = models.IntegerField()

class Orders(models.Model):
    surname = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    books = models.ManyToManyField(Books, through='OrderedBooks', related_name='orders')

class OrderedBooks(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
