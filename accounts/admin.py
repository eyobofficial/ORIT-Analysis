from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Profile


User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'username', 'get_full_name',
        'is_active', 'is_staff', 'is_superuser'
    )
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    inlines = (ProfileInline, )
