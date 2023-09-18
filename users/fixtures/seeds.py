import random

from django.contrib.auth.models import User
from faker import Faker


# Iniciar Faker
fake = Faker('pt_BR')

# 1. Criar superusuário
User.objects.create_superuser(
    username='admin',
    email='admin@email.com',
    password='admin',
    first_name='Admin',
    last_name='Admin',
)

# 2. Criar usuários e seus perfis
for _ in range(10):
    username = fake.user_name()
    email = fake.email()
    user = User.objects.create_user(
        username=username,
        email=email,
        password='123456',
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )