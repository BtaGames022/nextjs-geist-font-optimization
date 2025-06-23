from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Loads sample product data'

    def handle(self, *args, **kwargs):
        sample_products = [
            {
                'code': 'FER-12345',
                'name': 'Taladro Percutor Bosch',
                'brand': 'Bosch',
                'price': 89000.99
            },
            {
                'code': 'FER-67890',
                'name': 'Martillo Stanley',
                'brand': 'Stanley',
                'price': 15000.00
            },
            {
                'code': 'FER-11223',
                'name': 'Sierra Circular Makita',
                'brand': 'Makita',
                'price': 129900.00
            }
        ]

        for product_data in sample_products:
            Product.objects.get_or_create(
                code=product_data['code'],
                defaults=product_data
            )
            
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data'))
