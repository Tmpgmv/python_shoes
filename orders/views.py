from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from orders.forms import OrderForm
from orders.models import Order


class OrderListView(ListView):
    model = Order


class OrderCreateView(SuccessMessageMixin,
                      CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order_list")
    success_message = "Заказ добавлен."


class OrderUpdateView(SuccessMessageMixin,
                      UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_list')
    success_message = "Заказ обновлен."