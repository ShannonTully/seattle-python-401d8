from rest_framework import generics
from .serializers import ProductSerializer
from shopper_products.models import Product


class ProductListApi(generics.ListAPIView):
    serializer_class = ProductSerializer

    # Simple queryset if we don't need to filter
    # queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
