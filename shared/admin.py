from django.contrib import admin

from .models import Activity, Contractor, Consultant, Client, Work


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title', 'description')


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'long_name')
    search_fields = ('short_name', 'long_name')


@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'long_name')
    search_fields = ('short_name', 'long_name')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'long_name')
    search_fields = ('short_name', 'long_name')
