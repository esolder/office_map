from rest_framework import routers

from .views import PlanViewSet, WorkplaceViewSet


router = routers.DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'workplaces', WorkplaceViewSet)

urlpatterns = []

urlpatterns += router.urls
