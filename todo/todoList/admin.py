from django.contrib import admin
from .models import User,Todo
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Todo)
admin.site.register(User,UserAdmin)


