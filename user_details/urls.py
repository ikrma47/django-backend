from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Details

router = DefaultRouter()
router.register('details', Details, basename='api')

urlpatterns = [
    path('api/', include(router.urls))
]
