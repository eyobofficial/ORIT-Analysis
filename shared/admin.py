from django.contrib import admin

from .models import Company, Activity, Work


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'long_name', 'type', 'owner')
    list_display_links = ('id', 'short_name')
    search_fields = ('short_name', 'long_name')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('name', )


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
