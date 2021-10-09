from django.contrib import admin
from .models import Staff, Resumes


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rollNo')


admin.site.register(Staff, StaffAdmin)


admin.site.register(Resumes)
