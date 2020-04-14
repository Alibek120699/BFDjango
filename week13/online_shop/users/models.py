from django.db import models
from django.contrib.auth.models import AbstractUser

from .constants import USER_ROLES, CUSTOMER


class MyUser(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=USER_ROLES, default=CUSTOMER)

    # def _try_to_create_profile(self, created):
    #     if created:
    #         Profile.objects.get_or_create(user=self)
    #
    # def save(self, *args, **kwargs):
    #     print('pre_save')
    #     print('post_save')


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    address = models.TextField(default='Almaty')
