from django.core.management.base import BaseCommand


from online_shop.api.models import Product


class Command(BaseCommand):
    help = 'Delete Product objects from table'

    def add_arguments(self, parser):
        parser.add_argument('product_ids', nargs='+', help='Product ids for delete')

    def handle(self, *args, **kwargs):

        for product_id in kwargs['product_ids']:
            try:
                p = Product.objects.get(id=product_id)
                p.delete()
                self.stdout.write(self.style.SUCCESS(f"Product id: {product_id} was deleted successfully"))
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Product id: {product_id} does not exists!"))