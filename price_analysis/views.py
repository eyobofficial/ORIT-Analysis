from django.views.generic import TemplateView

from .mixins import BasePriceAnalysisMixin


class OverviewView(BasePriceAnalysisMixin, TemplateView):
    template_name = 'price_analysis/overview.html'
