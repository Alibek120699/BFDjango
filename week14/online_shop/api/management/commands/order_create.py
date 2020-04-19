import random

from django.core.management.base import BaseCommand

from api.models import ProductOrder


class Command(BaseCommand):
    help = 'Create data for Product Order Table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of product orders for creation')

    def handle(self, *args, **options):
        total = options['total']

        for i in range(total):
            o = ProductOrder.objects.create(discount=10,
                                            item_id=1,
                                            price=1000,
                                            delivery_price=200,
                                            quantity=4)
            self.stdout.write(f'Product Order {o.id} was created')
