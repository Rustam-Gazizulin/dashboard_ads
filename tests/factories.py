import factory.django

from ads.models import Ads, User, Selection


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'test_firstname',
    last_name = 'test_lastname',
    username = 'test_username',
    email = 'test@mail.ru',
    password = 'test123',
    birth_date = factory.Faker('date_object')


class SelectionFactory(factory.django.DjangoModelFactory):
    name = 'testselectionnew'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Selection


class AdsFactory(factory.django.DjangoModelFactory):
    name = 'testnewtest'
    author = factory.SubFactory(UserFactory)
    price = 12345

    class Meta:
        model = Ads





