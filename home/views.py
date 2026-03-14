from django.views.generic import ListView  # PREP

from products.models import Product


class HomeView(ListView):  # PREP
    template_name = "home/home.html"  # PREP
    model = Product