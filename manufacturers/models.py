from django.db import models


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=300,
                                         verbose_name="Наименование")

    def __str__(self):
        return self.manufacturer_name
