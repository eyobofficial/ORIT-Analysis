from .mixins import DashboardMixin


class OverviewView(DashboardMixin):
    template_name = 'dashboard/overview.html'
