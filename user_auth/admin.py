from django.contrib import admin
from online_courses.user_auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.Register(User,UserAdmin)