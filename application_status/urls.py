from django.urls import path, include
from .views import ApplicationStatusView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('application-status', ApplicationStatusView, basename='api')

urlpatterns = [path('api/', include(router.urls))]
