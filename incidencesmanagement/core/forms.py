from django import forms
from django.apps import apps

Department = apps.get_model('departments', 'Department')


class UserEmployeeCreationForm(forms.Form):
    """Form for User creation"""

    username = forms.CharField(max_length=50, required=True, label='')
    first_name = forms.CharField(max_length=50, required=True, label='')
    last_name = forms.CharField(max_length=50, required=True, label='')
    email = forms.EmailField(required=True, label='')
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        empty_label="Select a Department",
                                        label='')
    password = forms.CharField(widget=forms.PasswordInput, strip=False, required=True, label='')
    password_again = forms.CharField(widget=forms.PasswordInput, strip=False, required=True, label='')

    username.widget.attrs.update({"class": "form-control", "placeholder": "Username", 'autocomplete': 'off'})
    first_name.widget.attrs.update({"class": "form-control", "placeholder": "First name", 'autocomplete': 'off'})
    last_name.widget.attrs.update({"class": "form-control", "placeholder": "Last name", 'autocomplete': 'off'})
    email.widget.attrs.update({"class": "form-control", "placeholder": "Email ( i.e employee_a@email.com )", 'autocomplete': 'off'})
    department.widget.attrs.update({"class": "form-control"})
    password.widget.attrs.update({"class": "form-control", "placeholder": "Password"})
    password_again.widget.attrs.update({"class": "form-control", "placeholder": "Same password as before"})
    
    error_messages = {
        "password_mismatch": "The two password fields didn't match",
        "password_strength": "Password must contain uppercase, lowercase, digits and at least one special character",
        "password_too_short": "Password must have 8+ characters",
        "department_required": "The department where the user belongs to is required"
    }


class UserEmployeeUpdateForm(forms.Form):
    """User update Form"""

    username = forms.CharField(max_length=50, required=True, label='')
    first_name = forms.CharField(max_length=50, required=True, label='')
    last_name = forms.CharField(max_length=50, required=True, label='')
    email = forms.EmailField(required=True, label='')
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        empty_label="Select a Department",
                                        label='')
    username.widget.attrs.update({"class": "form-control", "placeholder": "Username",  'autocomplete': 'off'})
    first_name.widget.attrs.update({"class": "form-control", "placeholder": "First name",  'autocomplete': 'off'})
    last_name.widget.attrs.update({"class": "form-control", "placeholder": "Last name",  'autocomplete': 'off'})
    email.widget.attrs.update({"class": "form-control", "placeholder": "Email ( i.e employee_a@email.com )",  'autocomplete': 'off'})
    department.widget.attrs.update({"class": "form-control"})

    error_messages = {
        "department_required": "The department where the user belongs to is required"
    }


class UserEmployeeChangePasswordForm(forms.Form):
    """Change User password Form"""

    password = forms.CharField(widget=forms.PasswordInput, strip=False, required=True, label='')
    password_again = forms.CharField(widget=forms.PasswordInput, strip=False, required=True, label='')

    password.widget.attrs.update({"class": "form-control", "placeholder": "Password"})
    password_again.widget.attrs.update({"class": "form-control", "placeholder": "Same password as before"})

    error_messages = {
        "password_mismatch": "The two password fields didn't match",
        "password_strength": "Password must contain uppercase, lowercase, digits and at least one special character",
        "password_too_short": "Password must have 8+ characters",
        "department_required": "The department where the user belongs to is required"
    }
