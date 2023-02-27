from django.urls import path

from ads import views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("<int:pk>/", views.UserRetrieveDestroyView.as_view()),
    path("create/", views.UserCreateView.as_view()),
    path("update/<int:pk>/", views.UserUpdateView.as_view()),

]
