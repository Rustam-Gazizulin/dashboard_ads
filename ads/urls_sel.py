from django.urls import path

from ads import views

urlpatterns = [
    path("", views.SelectionListView.as_view(), name='selection_list'),
    path("<int:pk>/", views.SelectionRetrieveView.as_view()),
    path("create/", views.SelectionCreateView.as_view(), name='selection_create'),
    path("update/<int:pk>/", views.SelectionUpdateView.as_view()),
]
