from django.contrib import admin
from .models import Incidence, IncidenceLevel, IncidenceStatus


admin.site.register(Incidence)
admin.site.register(IncidenceLevel)
admin.site.register(IncidenceStatus)

