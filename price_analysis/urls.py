from django.urls import path

from .views import OverviewView


app_name = 'price_analysis'

urlpatterns = [
    path('', OverviewView.as_view(), name='overview'),
]
