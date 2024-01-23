from django.contrib.auth.models import User
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Plan, Workplace
from .serializers import (
    PlanSerializer,
    PlanListSerializer,
    WorkplaceSerializer,
    UserSerializer,
)


class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PlanListSerializer
        return PlanSerializer
    

class WorkplaceViewSet(ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
