from django.db import models


class BaseProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1000)
    desc = models.TextField(max_length=500)
    count = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        abstract = True

    def __str__(self):
        return self.name

    def get_description(self):
        raise NotImplementedError('you must implement this method')


class OnlineProduct(BaseProduct):
    needs_delivery = models.BooleanField(default=False)
    delivery_address = models.CharField(max_length=100)
    delivery_price = models.IntegerField(default=0)

    objects = models.Manager()

    def get_description(self):
        return self.desc[:20]


class OfflineProduct(BaseProduct):
    discount = models.IntegerField(default=10)

    objects = models.Manager()

    def get_description(self):
        return f'{self.name} (available online)'
