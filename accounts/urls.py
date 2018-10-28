from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import AuthenticationView


app_name = 'accounts'


urlpatterns = [
    path('login/', AuthenticationView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
