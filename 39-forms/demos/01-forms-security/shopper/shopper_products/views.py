from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from .forms import ProductForm
from .models import Product


class StoreView(LoginRequiredMixin, ListView):
    template_name = 'store/store.html'
    context_object_name = 'products'

    # Used to redirect the user if not logged in
    login_url = reverse_lazy('auth_login')


    # simplified queryset for overwriting the get_queryset()
    # queryset = Product.objects.filter(published='PUBLIC')

    # NO LONGER NECESSARY WITH LOGINREQUIREDMIXIN
    # def get(self, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return redirect('home')

    #     return super().get(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cover'] = settings.STATIC_URL + 'default_cover.thumbnail'
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'store/product_detail.html'
    model = Product
    login_url = reverse_lazy('auth_url')
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cover'] = settings.STATIC_URL + 'default_cover.thumbnail'
        return context

    def get_queryset(self):
        return Product.objects.filter(published='PUBLIC')


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'store/product_create.html'
    model = Product
    form_class = ProductForm
    success_url = 'store'
    login_url = reverse_lazy('auth_login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
