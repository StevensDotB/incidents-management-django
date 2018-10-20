from django import forms
from django.apps import apps

Department = apps.get_model('departments', 'Department')


class UserEmployeeCreationForm(forms.Form):
    """Form for User employee creation"""

    username = forms.CharField(max_length=50, required=True, label='')
    first_name = forms.CharField(max_length=50, required=True, label='')
    last_name = forms.CharField(max_length=50, required=True, label='')
    email = forms.EmailField(required=True, label='')
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        empty_label="Select a Department",
                                        required=True, label='')
    password = forms.CharField(widget=forms.PasswordInput, strip=False, required=True, label='')
    password_again = forms.CharField(widget=forms.PasswordInput, strip=False, required=True, label='')

    username.widget.attrs.update({"class": "form-control", "placeholder": "Username"})
    first_name.widget.attrs.update({"class": "form-control", "placeholder": "First name"})
    last_name.widget.attrs.update({"class": "form-control", "placeholder": "Last name"})
    email.widget.attrs.update({"class": "form-control", "placeholder": "Email ( i.e employee_a@email.com )"})
    department.widget.attrs.update({"class": "form-control"})
    password.widget.attrs.update({"class": "form-control", "placeholder": "Password"})
    password_again.widget.attrs.update({"class": "form-control", "placeholder": "Same password as before"})
    
    error_messages = {
        "password_mismatch": "The two password fields didn't match",
    }

