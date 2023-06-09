#pylint: disable=missing-module-docstring
#pylint: disable=line-too-long
#pylint: disable=trailing-newlines
#pylint: disable=missing-class-docstring
from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'date_time_in', 'date_time_out', 'duration', 'ProjectId_id', 'is_approved')


admin.site.register(Employee, EmployeeAdmin)


