from django.urls import path, include
from .views import AdminDashboardView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('dashboard', AdminDashboardView, basename='admin')

urlpatterns = [path('api/admin/', include(router.urls))]
