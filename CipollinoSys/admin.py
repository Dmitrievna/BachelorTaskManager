from django.contrib import admin
from .models import Person,Task
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Person

class UserPerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active')
#    list_filter = ('date_joined', 'last_login', 'is_staff', 'is_superuser', 'is_active',)
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserPerAdmin)
admin.site.register(Task)