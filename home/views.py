from django.views.generic import ListView  # PREP

from products.models import Product


class HomeView(ListView):  # PREP
    model = Product
    template_name = "home/home.html"  # PREP
