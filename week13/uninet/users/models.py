from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from .constants import USER_ROLES_CHOICES, STUDENT, TEACHER, OFFICE_REGISTER
from .validators import validate_file_size


class MyUserManager(UserManager):
    def get_students(self):
        return self.filter(role=STUDENT)

    def get_teachers(self):
        return self.filter(role=TEACHER)

    def get_office_registers(self):
        return self.filter(role=OFFICE_REGISTER)

    # def create_user(self, username, email=None, password=None, **extra_fields):
    #     if not username:
    #         raise ValueError('Username is required')
    #
    #     user = self.model(username=username, must_change_password=True, deleted=False,)
    #     return user


class MyUser(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=USER_ROLES_CHOICES)


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    ava = models.ImageField(upload_to='profile_files',
                            validators=[validate_file_size],
                            null=True, blank=True)

    def __str__(self):
        return self.user
