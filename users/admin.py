from django.contrib import admin

from users.models import Employee, User


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = (
        ('full_name', 'phone_number'),
        'job_title'
    )
    search_fields = ('full_name', 'phone_number')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        ('first_name', 'last_name'),
        'username',
        'email',
        'phone_number'
    )
    search_fields = ('first_name', 'last_name', 'phone_number')
