from django.urls import path

from ads import views

urlpatterns = [
    path("", views.CategoryView.as_view()),
    path("<int:pk>/", views.CategoryDetailView.as_view()),
]