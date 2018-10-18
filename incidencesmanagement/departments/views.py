from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from .forms import DepartmentForm
from .models import Department


class DepartmentCreate(CreateView):
    model = Department
    form_class = DepartmentForm



