
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','subbujobsproject.settings')
import django
django.setup()

from testapp.models import Hydjobs
from testapp.models import Bngjobs
from testapp.models import Punejobs
from faker import Faker
from random import *
fake = Faker()
def phonumbergen():
    d1 = randint(6,9)
    num = '' + str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead', 'Software Engineer','Associate Engineer','Python Web Developer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd','Mahesh Sir Student'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonumbergen()
        Hydjobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber)
        Bngjobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber)
        Punejobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber)


n = int(input('Enter number of records:'))
populate(n)
print(f'{n} records inserted successsfully....')
