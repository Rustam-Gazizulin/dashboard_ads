from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ads, User, Location, Selection
from ads.permissions import IsOwnerOrModerator
from ads.serializers import LocationSerializer, CategorySerializer, AdsSerializer, AdsCreateSerializer, \
    AdsUpdateSerializer, AdsDestroySerializer, UserSerializer, UserRetrieveSerializer, UserCreateSerializer, \
    UserUpdateSerializer, SelectionSerializer, SelectionRetrieveSerializer, SelectionCreateSerializer, \
    SelectionUpdateSerializer


def main(request):
    return JsonResponse({"status": "ok"}, status=200)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class AdsListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    def get(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat', [])
        if categories:
            self.queryset = self.queryset.filter(category__in=categories)
        search_name = request.GET.get('text')
        if search_name:
            self.queryset = self.queryset.filter(name__icontains=search_name)
        location_search = request.GET.get('loc')
        if location_search:
            self.queryset = self.queryset.filter(author__location_id__name__icontains=location_search)
        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_from:
            self.queryset = self.queryset.filter(Q(price__gte=price_from) & Q(price__lte=price_to))

        return super().list(request, *args, **kwargs)


class AdsRetrieveView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]


class AdsCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsCreateSerializer


class AdsUpdateView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]


@method_decorator(csrf_exempt, name='dispatch')
class AdsImageUpload(UpdateView):
    model = Ads
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category": self.object.category_id,
            "image": self.object.image.url if self.object.image else None
        })


class AdsDestroyView(DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsDestroySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionRetrieveView(RetrieveDestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionRetrieveSerializer
    permission_classes = [IsAuthenticated]


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]















