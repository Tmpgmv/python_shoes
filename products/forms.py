from concurrency.forms import ConcurrentForm
from django import forms

from products.models import Product
from suppliers.models import Supplier


class ProductForm(ConcurrentForm):
    class Meta:
        model = Product
        exclude = ["pk", ]


class SearchSortFilterForm(forms.Form):
    CHOICES = [
        ('more', 'Больше'),
        ('less', 'Меньше'),
    ]

    stock = forms.ChoiceField(
        choices=CHOICES,
        initial='more',
        required=False,
        label="Количество на складе"
    )

    search = forms.CharField(required=False,
                             label="Поиск")

    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(),
                                      empty_label="Все поставщики",
                                      required=False,
                                      label="Поставщик")
