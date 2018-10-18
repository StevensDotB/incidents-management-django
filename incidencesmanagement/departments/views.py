from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import DepartmentForm
from .models import Department


class DepartmentListView(ListView):
    model = Department
    paginate_by = 20


class DepartmentCreate(CreateView):
    model = Department
    form_class = DepartmentForm

    def get_success_url(self, *args):
        return reverse_lazy('departments:departments') + '?created'



