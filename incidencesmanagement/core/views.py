from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import UserEmployee
from .forms import (UserEmployeeCreationForm,
                    UserEmployeeChangePasswordForm,
                    UserEmployeeUpdateForm)


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


class UserCreateView(TemplateView):
    """User employee creation"""
    template_name = 'core/useremployee_form.html'

    def get(self, request, *args):
        form = UserEmployeeCreationForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        error = ''
        form = UserEmployeeCreationForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['department']:
                error = form.error_messages['department_required']

            elif form.cleaned_data['password'] and form.cleaned_data['password_again'] \
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

                return HttpResponseRedirect(reverse_lazy('users:users') + '?action=created')

        return render(request, self.template_name, {'form': form, 'error': error})


class UserUpdateView(TemplateView):
    """User update view"""
    template_name = 'core/useremployee_update_form.html'

    def get(self, request, *args, **kwargs):

        user = User.objects.get_by_natural_key(kwargs['username'])
        # Get user fields value
        form = UserEmployeeUpdateForm(initial={
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'department': user.useremployee.department
        })
        return render(request, self.template_name, {'form': form, 'username': kwargs['username']})

    def post(self, request, *args, **kwargs):
        error = ''
        form = UserEmployeeUpdateForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['department']:
                error = form.error_messages['department_required']
            else:
                user = User.objects.get_by_natural_key(form.cleaned_data['username'])
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['email']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                user_employee = UserEmployee.objects.get(user=user)
                user_employee.department = form.cleaned_data['department']
                user_employee.save()

                return HttpResponseRedirect(reverse_lazy('users:users') + '?action=updated')

        return render(request, self.template_name, {'form': form, 'error': error})


class UserChangePassword(TemplateView):
    """User change password view"""
    template_name = 'core/useremployee_change_password.html'

    def get(self, request, **kwargs):
        form = UserEmployeeChangePasswordForm
        return render(request, self.template_name, {'form': form, 'username': kwargs['username']})

    def post(self, request, *args, **kwargs):
        """Send data"""
        error = ''
        form = UserEmployeeChangePasswordForm(request.POST)
        username = request.POST.get('username')

        if form.is_valid():
            if form.cleaned_data['password'] and form.cleaned_data['password_again'] \
                    and form.cleaned_data['password_again'] != form.cleaned_data['password']:
                error = form.error_messages['password_mismatch']

            else:
                user = User.objects.get_by_natural_key(username)
                user.set_password(form.cleaned_data['password'])
                user.save()

                return HttpResponseRedirect(reverse_lazy('users:update', args=[username]) + '?action=password_changed')

        return render(request, self.template_name, {'form': form, 'error': error, 'username': username})


class UserDeleteView(DeleteView):
    """User delete view"""
    model = UserEmployee

    def get_success_url(self):
        return reverse_lazy('users:users') + '?action=deleted'
