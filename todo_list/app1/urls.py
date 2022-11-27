from django.urls import path
from . import views


urlpatterns = [
    path("", views.loginPage, name="login"),
    path("create-task/", views.create_task, name="create-task"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logOutUser, name="logout"),
    path("profile/<str:pk>/", views.userProfile, name="profile"),
    path("delete/<str:pk>/", views.delete_task, name="delete"),
    path("register/", views.register, name="register"),
]
