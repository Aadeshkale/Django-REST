from django.contrib import admin
from django.urls import path,re_path,include
from rest_framework import routers
from myapp.views import EmpView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp',EmpView.as_view(),name='emp'),
]
