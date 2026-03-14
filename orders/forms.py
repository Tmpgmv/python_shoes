from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['code', ]
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'),),
            'delivery_date': forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'),),
        }