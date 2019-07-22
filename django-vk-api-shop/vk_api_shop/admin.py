from django.contrib import admin

from .models import ParamsModel


@admin.register(ParamsModel)
class ParamsAdmin(admin.ModelAdmin):
    pass
