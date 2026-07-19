from django.urls import path
from . import views

urlpatterns = [
    path("create-user/", views.create_user, name="create_user"),
    path("show-users/", views.show_users, name="show_users"),
]