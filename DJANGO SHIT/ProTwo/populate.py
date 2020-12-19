import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakergen = Faker()

def populate(N=5):

    for entry in range(N):

        fake_name = fakergen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakergen.email()

        users = User.objects.get_or_create(fname=fake_fname, lname=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print('Populating')
    populate(50)
    print('Populating complete')