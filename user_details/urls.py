from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DetailsViewSet, UpdateCourseCategory, UpdateImage

router = DefaultRouter()
router.register('profile', DetailsViewSet, basename='api')
router.register('update-course-category', UpdateCourseCategory, basename='api')
router.register('update-profile-picture', UpdateImage, basename='api')

urlpatterns = [
    path('api/', include(router.urls))
]
