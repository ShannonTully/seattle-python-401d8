from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Product, Photo
from django.conf import settings
from .forms import ProductForm


class StoreView(ListView):
    template_name = 'store/store.html'
    context_object_name = 'products'
    # simplified queryset for overwriting the get_queryset()
    # queryset = Product.objects.filter(published='PUBLIC')

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cover'] = settings.STATIC_URL + 'default_cover.thumbnail'

        return context


# I would refactor this into a class view normally... we don't have time today.
def product_detail_view(request, pk=None):
    if not request.user.is_authenticated:
        return redirect('home')

    context = {
        'product': get_object_or_404(Product, id=pk),
        'photos': Photo.objects.filter(product__id=pk),
    }

    return render(request, 'store/product_detail.html', context)


class ProductCreateView(CreateView):
    template_name = 'store/product_create.html'
    model = Product
    form_class = ProductForm
    success_url = 'store'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
