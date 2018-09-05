from django.db import models
from django.contrib.auth.models import User


class ShopperProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    street = models.CharField(max_length=1024, null=True, blank=True)
    city = models.CharField(max_length=1024, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.CharField(max_length=14, null=True, blank=True)
    cell = models.CharField(max_length=20, null=True, blank=True)
    # home = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def active(cls):
        return cls.objects.filter(is_active=True)
