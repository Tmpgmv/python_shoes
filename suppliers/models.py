from django.db import models


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=300,
                                     verbose_name="Наименование")

    def __str__(self):
        return self.supplier_name
