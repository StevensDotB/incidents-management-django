from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import UserEmployee
from .forms import UserEmployeeCreationForm


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


class UserCreate(TemplateView):
    """User employee creation"""
    template_name = 'core/useremployee_form.html'

    def get(self, request):
        form = UserEmployeeCreationForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        error = ''
        form = UserEmployeeCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] and form.cleaned_data['password_again'] \
                    and form.cleaned_data['password_again'] != form.cleaned_data['password']:
                error = form.error_messages['password_mismatch']
            else:
                user = User(username=form.cleaned_data['username'],
                            email=form.cleaned_data['email'],
                            first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'])
                user.set_password(form.cleaned_data['password'])
                user.save()
                user_employee = UserEmployee(user=user, department=form.cleaned_data['department'])
                user_employee.save()

                return HttpResponseRedirect(reverse_lazy('core_users_list') + '?action=created')

        return render(request, self.template_name, {'form': form, 'error': error})











    

