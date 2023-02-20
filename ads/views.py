import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category, Ads, User
from dashboard_ads import settings


def main(request):
    return JsonResponse({"status": "ok"}, status=200)


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_text = request.GET.get('text', None)
        if search_text:
            self.object_list = self.object_list.filter(name__icontains=search_text)
        self.object_list = self.object_list.order_by('name')
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        categories = []
        for cat in page_obj:
            categories.append({
                "id": cat.id,
                "name": cat.name
            })
        response = {
            "items": categories,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }
        return JsonResponse(response, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data['name']
        )

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)

        self.object.name = category_data['name']

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"object delete": "status OK"})


class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        search_text = request.GET.get('text', None)
        if search_text:
            self.object_list = self.object_list.filter(name__icontains=search_text)

        self.object_list = self.object_list.select_related('author').select_related('category').order_by('-price')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "author": ad.author.username,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "category": ad.category.name,
                "image": ad.image.url if ad.image else None
            })

        response = {
            "items": ads,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }
        return JsonResponse(response, safe=False)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author_id": ads.author_id,
            "author": ads.author.username,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "category_id": ads.category_id,
            "category": ads.category.name,
            "image": ads.image.url if ads.image else None
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdsCreateView(CreateView):
    model = Ads
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)

        author = get_object_or_404(User, pk=ads_data['author_id'])
        category = get_object_or_404(Category, pk=ads_data['category_id'])

        ads = Ads.objects.create(
            name=ads_data['name'],
            price=ads_data['price'],
            description=ads_data['description'],
            is_published=ads_data['is_published'] if 'is_published' in ads_data else False,
            author=author,
            category=category
            )

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author.username,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "category": ads.category.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdsUpdateView(UpdateView):
    model = Ads
    fields = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ads_data = json.loads(request.body)

        author = get_object_or_404(User, pk=ads_data['author_id'])
        category = get_object_or_404(Category, pk=ads_data['category_id'])

        self.object.name = ads_data['name']
        self.object.author = author
        self.object.price = ads_data['price']
        self.object.description = ads_data['description']
        self.object.category = category

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


@method_decorator(csrf_exempt, name='dispatch')
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)







