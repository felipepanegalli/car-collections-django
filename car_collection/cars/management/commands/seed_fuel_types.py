from datetime import datetime
from django.core.management.base import BaseCommand
from car_collection.cars.models import FuelType


class Command(BaseCommand):
    help = 'Comando que ajuda a popular o banco de dados'

    # def add_arguments(self, parser):
    #     Caso seja usado alguma argumento no caso do faker por exemplo, para gerar N registros

    def handle(self, *args, **options):
        fuel_type = (
            ('Gasolina', 'Adtivada', datetime.now()),
            ('Etanol', '90%', datetime.now()),
            ('Diesel', 'S10', datetime.now()),
            ('Gás', 'Veícular', datetime.now()),
        )

        for fuel, description, pub_date in fuel_type:
            obj = FuelType.objects.create(
                type=fuel,
                description=description,
                pub_date=pub_date,
            )
            self.stdout.write(self.style.SUCCESS('"%s" criado com sucesso.' % obj.description))
