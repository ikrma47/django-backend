from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramPreferenceViewSet, PreferenceListViewSet

router = DefaultRouter()
router.register('preferences', ProgramPreferenceViewSet, basename='api')
router.register('preference-list', PreferenceListViewSet, basename='api')

urlpatterns = [
    path('api/', include(router.urls))
]
