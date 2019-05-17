import django_filters

from .models import Company


class CompanyFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Company
        fields = ('type', )
