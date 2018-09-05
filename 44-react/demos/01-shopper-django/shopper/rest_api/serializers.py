from rest_framework import serializers
from shopper_products.models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    cover = serializers.HyperlinkedIdentityField(
        view_name='photo-detail',
        lookup_url_kwarg='pk'
    )

    user = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_url_kwarg='username'
    )

    class Meta:
        model = Product
        fields = ('id', 'cover', 'user', 'name', 'description', 'price')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user
