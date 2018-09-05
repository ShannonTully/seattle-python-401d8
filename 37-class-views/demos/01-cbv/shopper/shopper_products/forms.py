from django.forms import ModelForm
from .models import Product, Photo


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['cover', 'name', 'description', 'price', 'published']

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['cover'].queryset = Photo.objects.filter(product__user__username=username)
