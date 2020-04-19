from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from .constants import USER_ROLES, CUSTOMER, SALESMAN


class MyUserManager(UserManager):
    def get_salesmen(self):
        return self.filter(role=SALESMAN)

    def get_customers(self):
        return self.filter(role=CUSTOMER)


class MyUser(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=USER_ROLES, default=CUSTOMER)

    objects = MyUserManager()


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    address = models.TextField(default='Almaty')
