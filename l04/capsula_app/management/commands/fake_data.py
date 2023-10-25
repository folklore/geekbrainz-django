from django.core.management.base import BaseCommand
from capsula_app.models import Client, Product, Order
import random
from django.db import transaction
from datetime import datetime, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile


class Command(BaseCommand):
    help = "Generate fake Clients, Products and Orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Users count')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        with transaction.atomic():
            for x in range(1, count + 1):
                client = Client(name=f'Name{x}',
                                email=f'mail{x}@mail.ru',
                                phone=f'(604) 401 {1234+x}',
                                address=f'address{x}',)
                client.save()

            for y in range(1, 1000 * count + 1):
                product = Product(title=f'Product{y}',
                                  description=f'Description{y} is bla bla bla many long text',
                                  cost=random.uniform(5.5, 275.5),
                                  count=random.randint(2, 27),
                                  cover=SimpleUploadedFile(name='image.jpg',
                                                           content=b"some image",
                                                           content_type='image/jpeg'))
                product.save()

            for z in range(1, 75 * count + 1):
                client = Client.objects.order_by('?').first()
                products = []

                for u in range(1, random.randint(2, 11)):
                    products.append(Product.objects.order_by('?').first())

                price = sum([product.cost for product in products])

                order = Order(client=client,
                              price=price)
                order.save()

                order.created_on=datetime.today() - timedelta(days=random.randint(1, 365))
                order.save()

                order.products.add(*products)
