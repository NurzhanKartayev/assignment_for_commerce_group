from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet, BossViewSet

app_name = 'todo'
router = DefaultRouter()

router.register(
    prefix=r'employee', viewset=EmployeeViewSet, basename='employee'
)

router.register(
    prefix=r'boss', viewset=BossViewSet, basename='boss'
)

urlpatterns = router.urls
