from django.contrib.auth.mixins import LoginRequiredMixin


class BaseViewMixin(LoginRequiredMixin):
    menu = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.menu
        return context
