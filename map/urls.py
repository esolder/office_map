from rest_framework import routers

from .views import PlanViewSet, WorkplaceViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'workplaces', WorkplaceViewSet)
router.register(r'users', UserViewSet)

urlpatterns = []

urlpatterns += router.urls
