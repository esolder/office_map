from rest_framework.viewsets import ModelViewSet

from .models import Plan, Workplace
from .serializers import (
    PlanSerializer,
    PlanListSerializer,
    WorkplaceSerializer,
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
