from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from django.urls import reverse

from post_office.admin import EmailAdmin
from post_office.models import Email

from .views import EmailPreview


class EmailPreviewAdmin(EmailAdmin):
    list_display = ('id', 'to_display', 'subject', 'template',
                    'status', 'last_updated', 'account_actions',)
    readonly_fields = ('account_actions',)
    search_fields = ('to', 'subject',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:pk>/preview/',
                self.admin_site.admin_view(EmailPreview.as_view()),
                name='preview_emails',
            ),
        ]
        return custom_urls + urls

    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}" target="_blank">Preview</a>',
            reverse('admin:preview_emails', kwargs={'pk': obj.pk}),
        )

    account_actions.short_description = 'Actions'
    account_actions.allow_tags = True


admin.site.unregister(Email)
admin.site.register(Email, EmailPreviewAdmin)
