from django.contrib import admin
from .models import Incidence, IncidenceLevel, IncidenceStatus, IncidenceStatusLog


class IncidenceAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update',)
    list_display = ('get_username',
                    'get_department',
                    'subject',
                    'message',
                    'get_level',
                    'get_status',
                    'create',
                    'update',)

    def get_username(self, instance):
        return instance.user.username

    def get_department(self, instance):
        return instance.user.useremployee.department.name

    def get_level(self, instance):
        return instance.level.name

    def get_status(self, instance):
        return instance.status.name

    get_username.short_description = 'User'
    get_department.short_description = 'Department'
    get_level.short_description = 'Level'
    get_status.short_description = 'Status'


class IncidenceStatusLogAdmin(admin.ModelAdmin):

    readonly_fields = ('update',)
    list_display = ('incidence',
                    'get_username',
                    'get_status',
                    'update',)

    def get_username(self, instance):
        return instance.user.username

    def get_status(self, instance):
        return instance.status.name

    get_username.short_description = 'User'
    get_status.short_description = 'Status'


admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(IncidenceLevel)
admin.site.register(IncidenceStatus)
admin.site.register(IncidenceStatusLog, IncidenceStatusLogAdmin)

