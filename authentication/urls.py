from .views import SignupView, LoginView
from django.urls import path


urlpatterns = [
    path('api/signup/', SignupView.as_view({'post': 'create'})),
    path('api/login/', LoginView.as_view())
]
