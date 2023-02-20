from django.urls import path

from ads import views

urlpatterns = [
    path("", views.AdsListView.as_view()),
    path("<int:pk>/", views.AdsDetailView.as_view()),
    path("create/", views.AdsCreateView.as_view()),
    path("update/<int:pk>/", views.AdsUpdateView.as_view()),
    path("upload/<int:pk>/", views.AdsImageUpload.as_view()),
    path("delete/<int:pk>/", views.AdsDeleteView.as_view()),
]
