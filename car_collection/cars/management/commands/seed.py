from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from car_collection.cars.models import Car, Brand, FuelType


class Command(BaseCommand):
    help = 'Comando que ajuda a popular o banco de dados'

    # def add_arguments(self, parser):
    #     Caso seja usado alguma argumento no caso do faker por exemplo, para gerar N registros

    def handle(self, *args, **options):
        obj = Brand.objects.create(
            name='Honda',
            pub_date=datetime.now()
        )

        self.stdout.write(self.style.SUCCESS('"%s" criado com sucesso.' % obj.name))
