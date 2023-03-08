import factory.django

from ads.models import Ads, User, Selection


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name"),
    last_name = factory.Faker("last_name"),
    username = factory.Faker("user_name"),
    email = factory.Faker("email"),
    password = factory.Faker("password", length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),
    birth_date = factory.Faker('date_object')


class SelectionFactory(factory.django.DjangoModelFactory):
    name = 'test_name'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Selection


class AdsFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name", length=15)
    author = factory.SubFactory(UserFactory)
    price = factory.Faker('pyint', min_value=100, max_value=10000)

    class Meta:
        model = Ads





