from django.urls import path

from ads import views

urlpatterns = [
    path("", views.AdsView.as_view()),
    path("<int:pk>/", views.AdsDetailView.as_view()),
]
