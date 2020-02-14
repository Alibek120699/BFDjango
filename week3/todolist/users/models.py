from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from rest_framework.authtoken.models import Token


class TodoUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'

class TodoUser2(User):
    pass

class TodoUser3(AbstractBaseUser):
    pass