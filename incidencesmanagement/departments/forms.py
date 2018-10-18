from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    """Department create and update form"""
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department name'})
        }
        labels = {
            'name': ''
        }

