from django.db import models

from .validators import validate_extension, validate_file_size


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}: {self.price}'

    class Meta:
        abstract = True


class Product(Item):
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    img = models.ImageField(upload_to='product_files',
                            validators=[validate_file_size],
                            null=True, blank=True)


class Service(Item):
    duration = models.PositiveIntegerField()
    extra_description = models.FileField(upload_to='product_files',
                                         validators=[validate_extension],
                                         null=True, blank=True)


class Order(models.Model):
    discount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'order#{self.id}'


class ServiceOrder(Order):
    item = models.ForeignKey(Service, on_delete=models.CASCADE)


class ProductOrder(Order):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField()
