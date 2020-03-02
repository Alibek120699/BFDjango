from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=1000)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Book(BookJournalBase):
    GENRE_CHOICES = (
        (1, 'Comedy'),
        (2, 'Melodrama')
    )
    num_pages = models.IntegerField()
    genre = models.IntegerField(choices=GENRE_CHOICES, default=1)


class Journal(BookJournalBase):
    TYPE_CHOICES = (
        (1, 'Bullet'),
        (2, 'Food'),
        (3, 'Travel'),
        (4, 'Sport')
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    publisher = models.CharField(max_length=100)
