from django.db import models


class OrderProduct(models.Model):

    order = models.ForeignKey("orders.Order",
                              on_delete=models.CASCADE,
                              verbose_name="Заказ")

    product = models.ForeignKey("products.Product",
                                on_delete=models.PROTECT,
                                verbose_name="Товар")

    amount = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 verbose_name="Количество")

    def __str__(self):
        return "Товар: " + str(self.product.pk) + ", " + "Заказ: " + str(self.order.pk)