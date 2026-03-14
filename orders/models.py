from django.db import models

# Create your models here.
class Order(models.Model):
    STATUSES = [("Новый", "Новый"), ("Завершен", "Завершен")]

    order_date = models.DateField(auto_now_add=True,
                                  verbose_name="Дата заказа")

    delivery_date = models.DateField(verbose_name="Дата доставки")

    office = models.ForeignKey('offices.Office',
                               on_delete=models.CASCADE,
                               verbose_name="Пункт выдачи:")

    client = models.ForeignKey('accounts.User',
                               on_delete=models.CASCADE,
                               verbose_name="Клиент")

    code = models.IntegerField(unique=True,
                               blank=True,
                               verbose_name="Код получения")

    status = models.CharField(max_length=10,
                              choices=STATUSES,
                              default='Новый',
                              verbose_name="Статус")

    def __str__(self):
        return "Заказ: " + str(self.pk)
