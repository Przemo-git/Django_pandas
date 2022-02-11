import random
import datetime

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

#We have to create at least 2 users

#Example when no exist data base:
#with parameters: 2 random users, 15 random products, time period since: 2020,1,1 -  2021,12,12,
#random quantity: 1: 500
#random price: 1: 500

#To create data use command: python manage.py createdata

from ...models import Product, Purchase


PRODUCTS = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]


class Provider(faker.providers.BaseProvider):

    def pandas_products(self):
        return self.random_element(PRODUCTS)


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):

        fake = Faker()
        fake.add_provider(Provider)


        for _ in range(15):
            d = fake.pandas_products()
            Product.objects.create(name=d)


        start_date = datetime.date(2020,1,1)
        end_date = datetime.date(2021,12,12)
        for i in range(15):
            id = random.randint(1, 15)
            Purchase.objects.create(
                product_id = id,
                salesman_id=random.randint(1,2),
                quantity=(random.randint(1,500)),
                price=(random.randint(1,500)),
                date=fake.date_between_dates(start_date,end_date)
            )




        check_products = Product.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of products: {check_products}"))













