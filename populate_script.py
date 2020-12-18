import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wishlist_api.settings')
django.setup()

from faker import Faker
import random
from wishlist_app.models import Client, Product

def creating_clients(clients_number):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(clients_number):
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        c = Client(name=name, email=email)
        c.save()

title_list = [
    'Liquidificador','Batedeira','Teclado',
    'Travesseiro','Fritadeira','Carregador',
    'Smartphone','Geladeira','Fogão',
    'Faqueiro','Panelas','Notebook','Cafeteira', 
    'Tablet','Ventilador' ]

brand_list = [
    'Arno','Samsung','Mondial',
    'Philco','Lg','Consul',
    'Tramontina','Britania','Sony',
    'Plumatex','Asus','Bosch','TCL', 
    'Electrolux', 'Motorola' ]

def creating_products(products_number):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(products_number):
        price = "{}".format(random.randrange(20, 1000))
        image = fake.image_url()
        brand = fake.word(ext_word_list=brand_list)
        title = fake.word(ext_word_list=title_list)
        reviewScore = "{}".format(random.randrange(0, 10))
        p = Product(price=price, image=image, brand=brand, title=title, reviewScore=reviewScore,)
        p.save()

creating_clients(50)
creating_products(50)
print('Dados criados!')