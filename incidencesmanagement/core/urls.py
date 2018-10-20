from django.urls import path
from .views import HomeView, UserListView, UserCreate

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='core_users_list'),
    path('users/create', UserCreate.as_view(), name='core_user_create'),
]
