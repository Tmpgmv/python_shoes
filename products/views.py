from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from general.mixins import ConcurrentUpdateMixin
from products.forms import ProductForm
from products.models import Product


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("home")
    success_message = "Товар добавлен."


class ProductUpdateView(SuccessMessageMixin,
                        ConcurrentUpdateMixin,
                        UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home')
    success_message = "Товар обновлен."


class ProductDeleteView(SuccessMessageMixin,
                        DeleteView):
    model = Product
    success_url = reverse_lazy('home')
    success_message = "Товар удален."