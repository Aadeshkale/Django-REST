from django.urls import path
from authapp.views import Access
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('access',Access.as_view()),
    path('auth-token',ObtainAuthToken.as_view()),
]