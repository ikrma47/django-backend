from django.urls import path, include
from .views import DocumentsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('document', DocumentsView, basename='api')

urlpatterns = [path('api/', include(router.urls))]
