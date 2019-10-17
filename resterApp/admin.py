from django.contrib import admin
from .modeler import ResterModel

class ResterAdmin(admin.ModelAdmin):
    list_display = ('meal', 'description', 'ordered')



admin.site.register(ResterModel, ResterAdmin)
