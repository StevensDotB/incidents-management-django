from django.urls import path
from .views import DepartmentCreate, DepartmentListView, DepartmentUpdate, DepartmentDelete


departments_patterns = ([
    path('', DepartmentListView.as_view(), name="departments"),
    path('create/', DepartmentCreate.as_view(), name="create"),
    path('<int:pk>/update/', DepartmentUpdate.as_view(), name="update"),
    path('<int:pk>/delete/', DepartmentDelete.as_view(), name="delete")
], 'departments')
