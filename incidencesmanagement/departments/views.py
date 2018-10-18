from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from .forms import DepartmentForm
from .models import Department
# ---------------------------
# CRUD Views for Departments
# ---------------------------


class DepartmentListView(ListView):
    """Display all Departments"""
    model = Department


class DepartmentCreate(CreateView):
    """Create a new Department"""
    model = Department
    form_class = DepartmentForm

    def get_success_url(self, *args):
        return reverse_lazy('departments:departments') + '?action=created'


class DepartmentUpdate(UpdateView):
    """Update/Edit a Department"""
    model = Department
    form_class = DepartmentForm
    template_name_suffix = '_update_form'

    def get_success_url(self, *args):
        return reverse_lazy('departments:departments') + '?action=updated'


class DepartmentDelete(DeleteView):
    """Delete a Department"""
    model = Department

    def get_success_url(self, *args):
        return reverse_lazy('departments:departments') + '?action=deleted'





