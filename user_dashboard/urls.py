from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardView

router = DefaultRouter()
router.register('dashboard', DashboardView, basename='api')

urlpatterns = [path('api/', include(router.urls))]
