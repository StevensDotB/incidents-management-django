from django.urls import path
from .views import DepartmentCreate, DepartmentListView


departments_patterns = ([
    path('', DepartmentListView.as_view(), name="departments"),
    path('create/', DepartmentCreate.as_view(), name="create")
], 'departments')
