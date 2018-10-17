from django.contrib import admin
from .models import Incidence, IncidenceLevel, IncidenceStatus


class IncidenceAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')
    list_display = ('get_username',
                    'subject',
                    'message',
                    'get_level',
                    'get_status',
                    'create',
                    'update')

    def get_username(self, instance):
        return instance.user.username

    def get_level(self, instance):
        return instance.level.name

    def get_status(self, instance):
        return instance.status.name

    get_username.short_description = 'User'
    get_level.short_description = 'Level'
    get_status.short_description = 'Status'


admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(IncidenceLevel)
admin.site.register(IncidenceStatus)

