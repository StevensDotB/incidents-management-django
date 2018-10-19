from django.urls import path
from .views import HomeView, UserListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='core_users_list'),
    # path('', HomeView.as_view(), name='home'),
]
