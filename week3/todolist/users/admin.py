from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'is_editor')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )
