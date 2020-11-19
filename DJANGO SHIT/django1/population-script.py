import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')

import django
django.setup()

import random
from app1.models import AccessRecord, Webpage, User
from faker import Faker

fakergen = Faker()
users = [1,2,3,4]

def add_user():
    u = User.objects.get_or_create(usr=random.choice(users))[0]
    u.save()
    return u

def populate(N=5):

    for entry in range(N):

        usr = add_user()

        fake_url = fakergen.url()
        fake_date = fakergen.date()
        fake_name = fakergen.company()

        webpg = Webpage.objects.get_or_create(user=usr, url=fake_url, name=fake_name)[0]
        accssrecord = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__== '__main__':
    print('populating script')
    populate(100)
    print('Populating finished')