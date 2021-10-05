from django.contrib import admin
from .models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rollNo')


admin.site.register(Staff, StaffAdmin)
