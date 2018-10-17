from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserEmployee, Department


class UserEmployeeInline(admin.StackedInline):
    model = UserEmployee
    can_delete = False
    verbose_name_plural = "Department"
    fields = ('department',)


class UserEmployeeAdmin(UserAdmin):
    inlines = (UserEmployeeInline,)
    readonly_fields = ('last_login', 'date_joined',)
    list_display = ('username',
                    'email',
                    'first_name',
                    'last_name',
                    'get_department',
                    'is_staff',
                    'last_login')

    def get_department(self, instance):
        return instance.useremployee.department.name

    get_department.short_description = 'Department'


admin.site.unregister(User)
admin.site.register(User, UserEmployeeAdmin)
admin.site.register(Department)
