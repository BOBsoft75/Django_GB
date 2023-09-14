from django.core.management.base import BaseCommand
from hw2_app.models import Client
from faker import Faker
import random


class Command(BaseCommand):
    help = "Generate fake clients."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        fake = Faker('ru_RU')
        for i in range(1, count + 1):

            client = Client(name=fake.name(),
                            email=fake.email(),
                            phone='+79' + str(random.randint(111111111, 999999999)),
                            address=fake.address(),
                            date_registration=fake.date())
            client.save()