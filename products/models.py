from decimal import Decimal

from concurrency.fields import IntegerVersionField
from django.core.validators import MinValueValidator
from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    PRODUCT_NAME_CHOICES = [("Ботинки", "Ботинки"),
                            ("Кеды", "Кеды"),
                            ("Кроссовки", "Кроссовки"),
                            ("Полуботинки", "Полуботинки"),
                            ("Сапоги", "Сапоги"),
                            ("Тапочки", "Тапочки"),
                            ("Туфли", "Туфли"),
                            ]
    UNIT_OF_MEASUREMENT_CHOICES = [("шт.", "шт.")]

    PRODUCT_CATEGORY_CHOICES = [("Женская обувь", "Женская обувь"),
                                ("Мужская обувь", "Мужская обувь")]

    sku = models.CharField(max_length=120,
                           verbose_name="Артикул", )
    product_name = models.CharField(max_length=120,
                                    choices=PRODUCT_NAME_CHOICES,
                                    verbose_name="Наименование товара", )
    unit_of_measurement = models.CharField(max_length=20,
                                           choices=UNIT_OF_MEASUREMENT_CHOICES,
                                           verbose_name="Единица измерения", )
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))],
                                verbose_name="Цена", )

    supplier = models.ForeignKey("suppliers.Supplier",
                                 on_delete=models.CASCADE,
                                 verbose_name="Поставщик", )

    manufacturer = models.ForeignKey("manufacturers.Manufacturer",
                                     on_delete=models.CASCADE,
                                     verbose_name="Производитель", )

    product_category = models.CharField(max_length=20,
                                        choices=PRODUCT_CATEGORY_CHOICES,
                                        verbose_name="Категория", )

    discount = models.DecimalField(max_digits=10,
                                   decimal_places=2,
                                   default=0,
                                   validators=[MinValueValidator(Decimal('0'))],
                                   verbose_name="Скидка", )

    stock = models.PositiveIntegerField(verbose_name="Количество на складе")

    description = models.CharField(max_length=400, verbose_name="Описание")

    photo = ResizedImageField(
        size=[300, 200],
        default='picture.png',
        verbose_name="Изображение",
    )

    version = IntegerVersionField()

    def __str__(self):
        return "" + str(self.pk) + ": " + self.product_name + ": " + self.description
