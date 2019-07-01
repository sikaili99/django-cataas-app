from django.contrib import admin
from .models import Cats


class CatsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


admin.site.register(Cats, CatsAdmin)
