import random
import string
from faker import Faker

faker = Faker()


def generate_username():
    return faker.name() + str(random.randint(10000, 999999)) + random.choice(string.ascii_lowercase)


def generate_email():
    email = faker.email()
    name, domain = email.split("@")
    name += str(random.randint(10000, 999999)) + random.choice(string.ascii_lowercase)
    return f"{name}@{domain}"


def generate_password():
    return faker.password(length=8, digits=True)
