from django.urls import path

from ads import views

urlpatterns = [
    path("", views.CategoryListView.as_view()),
    path("<int:pk>/", views.CategoryDetailView.as_view()),
    path("create/", views.CategoryCreateView.as_view()),
    path("update/<int:pk>/", views.CategoryUpdateView.as_view()),
    path("delete/<int:pk>/", views.CategoryDeleteView.as_view()),
]
