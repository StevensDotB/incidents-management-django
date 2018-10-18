from django.urls import path
from .views import DepartmentCreate


departments_patterns = ([
    path('create/', DepartmentCreate.as_view())
], 'departments')
