from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExperienceViewSet

router = DefaultRouter()
router.register('experience', ExperienceViewSet, basename='api')

urlpatterns = [
    path('api/', include(router.urls))
]
