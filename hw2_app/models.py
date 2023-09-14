from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    name = models.CharField(max_length=26)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_registration = models.DateField()

    def __str__(self):
        return f'{self.email.lower()}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.IntegerField()
    date_receipt = models.DateField()

    def __str__(self):
        return f'{self.name.capitalize()}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    product = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_order = models.DateField()

    def __str__(self):
        return f'Заказ #{self.pk} - {self.client.email.lower()}'

    class Meta:
        ordering = ('-date_order',)
