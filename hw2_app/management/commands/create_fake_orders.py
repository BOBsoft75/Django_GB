from django.core.management.base import BaseCommand
from hw2_app.models import Client, Product, Order
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generate fake order.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        fake = Faker()
        for i in range(1, count + 1):
            client = Client.objects.order_by('?').first()
            total_amount = 0
            products = Product.objects.order_by('?')[:random.randint(2, 5)]
            for product in products:
                total_amount += product.price
            order = Order.objects.create(
                client=client,
                total_amount=total_amount,
                date_order=f'20{random.randint(1, 23):02}-{random.randint(1, 8):02}-{random.randint(1, 28):02}'
            )
            order.product.set(products)
