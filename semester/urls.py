from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(basename='api')

urlpatterns = [
    path('api/', include(router.urls))
]
