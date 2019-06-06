from django.urls import path
from .views import (HomeView,
                    UserListView,
                    UserCreateView,
                    UserUpdateView,
                    UserChangePassword,
                    UserDeleteView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

# Users urls
users_urlpatterns = ([
     path('', UserListView.as_view(), name='users'),
     path('create/', UserCreateView.as_view(), name='create'),
     path('<username>/edit/', UserUpdateView.as_view(), name='update'),
     path('<username>/change_password/', UserChangePassword.as_view(), name='change_password'),
     path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
], 'users')
