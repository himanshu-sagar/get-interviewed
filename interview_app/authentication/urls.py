from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePassword, SendPaswordResetEmailView, UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change_password/', UserChangePassword.as_view(), name='change_password'),
    path('send_reset_email/', SendPaswordResetEmailView.as_view(), name='send_reset_password_email'),
    path('reset_password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset_password')
]
