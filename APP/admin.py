from django.contrib import admin
from . models import UserProfile
from APP.models import UserProfile

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'email', 'password',]