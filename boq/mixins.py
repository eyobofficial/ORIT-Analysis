from django.views.generic import TemplateView

from shared.mixins import BaseViewMixin


class BaseBoqMixin(BaseViewMixin):
    menu = 'boq'
