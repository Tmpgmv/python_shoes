from django.contrib.postgres.search import SearchVector
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

    def get_queryset(self):
        sort_by_stock = self.request.GET.get("stock", "more")
        search_phrase = self.request.GET.get("search", None)
        supplier_id = self.request.GET.get("supplier", None)

        queryset = super().get_queryset()

        if sort_by_stock == "more":
            queryset = queryset.order_by("-stock")
        else:
            queryset = queryset.order_by("stock")

        if supplier_id:
            queryset = queryset.filter(supplier_id=supplier_id)

        if search_phrase:
            queryset = queryset.annotate(search=SearchVector('sku',
                                                             'product_name',
                                                             'unit_of_measurement',
                                                             'product_category',
                                                             'description')).filter(
                search__icontains=search_phrase)

        return queryset