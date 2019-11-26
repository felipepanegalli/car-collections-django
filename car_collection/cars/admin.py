from django.contrib import admin
from car_collection.cars.models import Car, Brand, FuelType

# Register your models here.
admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(FuelType)
