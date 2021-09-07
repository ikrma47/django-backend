from .views import SignupView, LoginView, VerifyEmailView
from django.urls import path


urlpatterns = [
    path('api/signup/', SignupView.as_view({'post': 'create'})),
    path('api/login/', LoginView.as_view()),
    path('api/verify-email/otp/', VerifyEmailView.as_view())
]
