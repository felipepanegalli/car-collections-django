from datetime import datetime
from django.core.management.base import BaseCommand
from car_collection.cars.models import Brand


class Command(BaseCommand):
    help = 'Comando que ajuda a popular o banco de dados'

    # def add_arguments(self, parser):
    #     Caso seja usado alguma argumento no caso do faker por exemplo, para gerar N registros

    def handle(self, *args, **options):
        brands = (
            ('Toyota', datetime.now()),
            ('Volkswagen', datetime.now()),
            ('Ford', datetime.now()),
            ('Nissan', datetime.now()),
        )
        for brand, pub_date in brands:
            obj = Brand.objects.create(
                name=brand,
                pub_date=pub_date,
            )
            self.stdout.write(self.style.SUCCESS('"%s" criado com sucesso.' % obj.name))
