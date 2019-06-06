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
        form_validated = True
        form = UserEmployeeCreationForm(request.POST)
        if form.is_valid():

            if not form.cleaned_data['department']:
                error = form.error_messages['department_required']

            password = form.cleaned_data['password']

            if password:
                uppercase = len([char for char in password if char.islower()])
                lowercase = len([char for char in password if char.isupper()])
                special_char = len([char for char in password if char in ",._-!$#*"])

                if uppercase < 1 or lowercase < 1 or special_char < 1:
                    error = form.error_messages['password_strength']
                    form_validated = False

                if len(password) < 8:
                    form_validated = False
                    error = form.error_messages['password_too_short']

                elif password and form.cleaned_data['password_again'] and form.cleaned_data['password_again'] != password:
                    error = form.error_messages['password_mismatch']

            if form_validated:
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
        form_validated = True
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
        valid_password = True
        form = UserEmployeeChangePasswordForm(request.POST)
        username = request.POST.get('username')

        if form.is_valid():

            password = form.cleaned_data['password']

            if password:
                uppercase = len([char for char in password if char.islower()])
                lowercase = len([char for char in password if char.isupper()])
                special_char = len([char for char in password if char in ",._-!$#*"])

                if uppercase < 1 or lowercase < 1 or special_char < 1:
                    error = form.error_messages['password_strength']
                    valid_password = False

                if len(password) < 8:
                    error = form.error_messages['password_too_short']
                    valid_password = False

                if password and form.cleaned_data['password_again'] and form.cleaned_data['password_again'] != password:
                    valid_password = False
                    error = form.error_messages['password_mismatch']

                if valid_password:
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
