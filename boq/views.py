from django.views.generic import TemplateView

from .mixins import BaseBoqMixin


class OverviewView(BaseBoqMixin, TemplateView):
    template_name = 'boq/overview.html'
