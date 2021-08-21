from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, DepartmentProgramViewSet

router = DefaultRouter()
router.register('department', DepartmentViewSet, basename='api')
router.register('program', DepartmentProgramViewSet, basename='api')

urlpatterns = [
    path('api/', include(router.urls))
]
