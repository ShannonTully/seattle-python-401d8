from django.test import TestCase

# Create your tests here.


# class ProfileFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = ShopperProfile

#     street = factory.Faker('street_address')
#     city = factory.Faker('city')
#     state = factory.Faker('state_abbr')
#     zip_code = factory.Faker('zipcode')
#     cell = factory.Faker('phone_number')
#     home = factory.Faker('phone_number')

def populate_profile(user, **kwargs):
    user.profile.street = kwargs['street'] if 'street' in kwargs else factory.Faker('street_address')
    user.profile.city = kwargs['city'] if 'city' in kwargs else factory.Faker('city')
    user.profile.state = kwargs['state'] if 'state' in kwargs else factory.Faker('state_abbr')
    user.profile.zip_code = kwargs['zip_code'] if 'zip_code' in kwargs else factory.Faker('zipcode')
    user.profile.cell = kwargs['cell'] if 'cell' in kwargs else factory.Faker('phone_number')
    user.profile.home = kwargs['home'] if 'home' in kwargs else factory.Faker('phone_number')
