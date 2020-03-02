from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, MyUserProfile


class InlineProfile(admin.StackedInline):
    model = MyUserProfile
    verbose_name = 'Profiles'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    inlines = (InlineProfile, )


@admin.register(MyUserProfile)
class MyUserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio',)