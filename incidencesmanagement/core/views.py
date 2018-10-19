from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import UserEmployee


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'core/index.html'


class UserListView(ListView):
    """Displays all users"""
    model = UserEmployee
    fields = ["username"
              "email",
              "first_name",
              "last_name",
              "department",
              "last_login",
              "date_joined"]

