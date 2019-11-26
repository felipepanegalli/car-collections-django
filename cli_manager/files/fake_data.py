from datetime import datetime

from car_collection.cars.models import Car, Brand, FuelType


def faker_brand():
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
        print(obj.name + ' criado.')


def faker_fuel_type():
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
        print(obj.name + ' criado.')


def faker_car():
    cars = (
        ('NISSAN FRONTIER SL CD 4X4', '2016', 'Silver', 4, 3, datetime.now()),
        ('VOLKSWAGEN GOLF HIGHLINE', '2017', 'Black', 2, 1, datetime.now()),
    )
    for name, year, color, brand, type_fuel, pub_date in cars:
        obj = Car.objects.create(
            name=name,
            year=year,
            color=color,
            brand=Brand.objects.get(brand),
            type_fuel=FuelType.objects.get(type_fuel),
            pub_date=pub_date,
        )
        print(obj.name + ' criado.')
