import random

from django.core.management.base import BaseCommand

from online_shop.api.models import Product, ShopStore


def create_shops(num=3):
    shops = [ShopStore(name=f'shop {i}',
                       address=f'Tole bi {random.randint(11, 59)}')
             for i in range(num)]

    ShopStore.objects.bulk_create(shops)


class Command(BaseCommand):
    help = 'Create data for Product Table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of products for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new products')

        parser.add_argument('-c', '--cheap', action='store_true', help='Create Product with cheap price')

    def handle(self, *args, **options):
        total = options['total']
        prefix = options.get('prefix')
        cheap = options.get('cheap')

        if not prefix:
            prefix = 'SM'  # SUPER MARKET

        create_shops(total)

        self.stdout.write()
        for i in range(total):
            if cheap:
                p = Product.objects.create(name=f'{prefix}_shop {i}',
                                           price=1000,
                                           shop_id=1,
                                           description='description',
                                           color='color',
                                           size='size')
            else:
                p = Product.objects.create(name=f'shop {i}',
                                           price=random.randint(2000, 5000),
                                           shop_id=1,
                                           description='description',
                                           color='color',
                                           size='size')
            self.stdout.write(f'Product {p.id} was created')
