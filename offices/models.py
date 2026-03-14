from django.db import models


class Office(models.Model):
    address = models.CharField(max_length=300,
                               verbose_name="Адрес")

    def __str__(self):
        return self.address
