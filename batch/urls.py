from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OfferedProgramsViewSet, BatchViewSet

router = DefaultRouter()
router.register('offered-programs', OfferedProgramsViewSet, basename='api')
router.register('batch', BatchViewSet, basename='api')

urlpatterns = [
    path('api/', include(router.urls))
]
