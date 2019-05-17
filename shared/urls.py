from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet, ActivityViewSet, WorkViewSet


app_name = 'shared'


router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'works', WorkViewSet)


urlpatterns = [
    path('', include(router.urls))
]
