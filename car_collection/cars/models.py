from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    color = models.CharField(max_length=50)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    type_fuel = models.ForeignKey('FuelType', on_delete=models.CASCADE)
    pub_date = models.DateTimeField()

    class Meta:
        db_table = 'cars_car'
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        db_table = 'cars_brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class FuelType(models.Model):
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, default='')
    pub_date = models.DateTimeField()

    class Meta:
        db_table = 'cars_fuel_types'
        verbose_name = 'Fuel type'
        verbose_name_plural = 'Fuel types'

    def __str__(self):
        return self.type
