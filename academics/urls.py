from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserAcademicRecordView

router = DefaultRouter()
router.register('academics', UserAcademicRecordView, basename='api')

urlpatterns = [
    path('api/', include(router.urls))
]
