from django.views.generic import ListView  # PREP

from products.forms import SearchSortFilterForm
from products.models import Product


class HomeView(ListView):  # PREP
    template_name = "home/home.html"  # PREP
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = SearchSortFilterForm(self.request.GET)
        context['form'] = form
        return context