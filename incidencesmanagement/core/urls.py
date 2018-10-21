from django.urls import path
from .views import (HomeView,
                    UserListView,
                    UserCreateView,
                    UserUpdateView,
                    UserChangePassword)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='core_users_list'),
    path('users/create', UserCreateView.as_view(), name='core_user_create'),
    path('users/<username>/edit', UserUpdateView.as_view(), name='core_user_update'),
    path('users/<username>/change_password', UserChangePassword.as_view(), name='core_user_change_password'),
]
