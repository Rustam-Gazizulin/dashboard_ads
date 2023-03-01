from django.urls import path

from ads import views

urlpatterns = [
    path("", views.SelectionListView.as_view()),
    path("<int:pk>/", views.SelectionRetrieveView.as_view()),
    path("create/", views.SelectionCreateView.as_view()),
    path("update/<int:pk>/", views.SelectionUpdateView.as_view()),
    # path("delete/<int:pk>/", views.SelectionDestroyView.as_view()),
]
