from django.db.models import Q

from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .filters import CompanyFilter
from .models import Company, Activity, Work
from .serializers import CompanySerializer, ActivitySerializer, WorkSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated, )
    filterset_class = CompanyFilter

    def get_queryset(self):
        """
        Return company instance they own OR have no owner at all
        """
        user = self.request.user
        return Company.objects.filter(Q(owner=None) | Q(owner=user))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, pk):
        """
        Ensure users can only edit the Company instance they own
        """
        company = Company.objects.get(pk=pk)
        if company.owner != request.user:
            raise PermissionDenied()
        return super().update(request, pk)

    def destroy(self, request, pk):
        """
        Ensure users can only delete the Company instance they own
        """
        company = Company.objects.get(pk=pk)
        if company.owner != request.user:
            raise PermissionDenied()
        return super().destroy(request, pk)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = (IsAuthenticated, )


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = (IsAuthenticated, )
