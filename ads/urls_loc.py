from django.urls import path

from ads import views

urlpatterns = [
    path("", views.LocationListView.as_view()),

]
