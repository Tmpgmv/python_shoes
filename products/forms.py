from concurrency.forms import ConcurrentForm

from products.models import Product


class ProductForm(ConcurrentForm):
    class Meta:
        model = Product
        exclude = ["pk",]