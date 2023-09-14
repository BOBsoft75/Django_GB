from django.core.management.base import BaseCommand
from hw2_app.models import Product
from faker import Faker
import random


class Command(BaseCommand):
    help = "Generate fake product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        fake = Faker('ru_RU')
        for i in range(1, count + 1):
            product = Product(name=f'Product {i} name {fake.text(max_nb_chars=25)}',
                              description=fake.text(max_nb_chars=1000),
                              price=round(random.uniform(0.01, 99999), 2),
                              store=random.randint(11, 999),
                              date_receipt=fake.date_between(start_date='-5y')
                              )
            product.save()
