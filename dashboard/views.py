from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView

from post_office.models import Email

from .mixins import DashboardMixin


class OverviewView(DashboardMixin):
    template_name = 'dashboard/overview.html'


class EmailPreview(DetailView):
    model = Email
    template_name = 'dashboard/email-preview.html'


class BaseEmailView(DetailView):
    url = None
    object = None
    email_class = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.email_class(self.object).send()
        message = 'The {} e-mail has been sent.'.format(self.email_name)
        messages.success(request, message)
        return redirect(reverse(self.url, args=(self.object.pk,)))
