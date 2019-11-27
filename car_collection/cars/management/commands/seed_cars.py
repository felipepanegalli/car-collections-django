from datetime import datetime
from django.core.management.base import BaseCommand
from car_collection.cars.models import FuelType, Car, Brand


class Command(BaseCommand):
    help = 'Comando que ajuda a popular o banco de dados'

    # def add_arguments(self, parser):
    #     Caso seja usado alguma argumento no caso do faker por exemplo, para gerar N registros

    def handle(self, *args, **options):
        cars = (
            ('NISSAN FRONTIER SL CD 4X4', '2016-01-01', 'Silver', 4, 3, datetime.now()),
            ('VOLKSWAGEN GOLF HIGHLINE', '2017-01-01', 'Black', 2, 1, datetime.now()),
        )
        for name, year, color, brand, type_fuel, pub_date in cars:
            obj = Car.objects.create(
                name=name,
                year=year,
                color=color,
                brand=Brand.objects.get(id=brand),
                type_fuel=FuelType.objects.get(id=type_fuel),
                pub_date=pub_date,
            )
            self.stdout.write(self.style.SUCCESS('"%s" criado com sucesso.' % obj.name))
