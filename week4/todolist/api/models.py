from django.db import models
from users.models import MyUser


class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Task(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)

    objects = TaskManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.title}: {self.done}'
