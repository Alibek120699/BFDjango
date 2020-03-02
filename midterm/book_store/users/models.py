from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    # USER_ROLES = (
    #     (1, 'admin'),
    #     (2, 'guest'),
    # )
    # role = models.IntegerField(choices=USER_ROLES, default=1)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class MyUserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
