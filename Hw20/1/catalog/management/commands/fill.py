import json
from django.core.management import BaseCommand
from catalog.models import Category, Product

file_json = 'catalog.json'

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """
        Получение данных из фикстуры с категориями:
        return: список с категориями
        """
        with open(file_json, 'r', encoding="utf-8") as file:
            categories = file.read()
        return json.loads(categories)

    @staticmethod
    def json_read_products():
        with open(file_json, 'r', encoding="utf-8") as file:
            products = file.read()
        return json.loads(products)

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()


        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            if category['model'] == 'catalog.category':
                category_for_create.append(
                    Category(id=category['pk'],
                             name=category["fields"]["name"],
                             description=category["fields"]["description"],
                             )
                )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            if product['model'] == 'catalog.product':
                product_for_create.append(
                    Product(pk=product["pk"],
                            name=product["fields"]["name"],
                            description=product["fields"]["description"],
                            price=product["fields"]["price"],
                            image=product["fields"]["image"],
                            category=Category.objects.get(pk=product["fields"]["category"]),
                            created_at=product["fields"]["created_at"],
                            updated_at=product["fields"]["updated_at"],
                            )
                )

        Product.objects.bulk_create(product_for_create)
