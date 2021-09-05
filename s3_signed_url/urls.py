from django.urls import path
from .views import GetPreSignedUrl

urlpatterns = [path('api/get-signed-url', GetPreSignedUrl.as_view())]