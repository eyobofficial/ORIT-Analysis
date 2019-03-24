from django.urls import path

from .views import OverviewView


app_name = 'bog'

urlpatterns = [
    path('', OverviewView.as_view(), name='overview'),
]
