import random
import datetime

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker


#żeby testować usuń bazę i migracje inicjujące tabele i stwórz drugiego usera testowgo
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
            #ze slug trzeba uważać bo może być np: Polo Shirt albo Polo&Shirt
            #ewentualnie można w modelu utworzyć slug

        start_date = datetime.date(2020,1,1)
        end_date = datetime.date(2021,12,12)
        for i in range(15):
            id = random.randint(1, 15)
            Purchase.objects.create(
                product_id = id,     #foreign key trzeba utworzyć id
                salesman_id=random.randint(1,2),    ########################### trzeba utworzyć drugiego dodatkowego usera w adminie + id(foreign key)
                quantity=(random.randint(1,500)),
                price=(random.randint(1,500)),
                date=fake.date_between_dates(start_date,end_date)
            )




        check_products = Product.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of products: {check_products}"))


#https://faker.readthedocs.io/en/master/




#żeby zbudować własnego providera:
#Najpierw import faker.providers, buduje listy: PRODUCTS


