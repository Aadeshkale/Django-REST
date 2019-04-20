from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import  Emp
from myapp.serializers import EmpSerializer
from rest_framework import viewsets


class EmpView(viewsets.ModelViewSet):
        queryset = Emp.objects.all()
        serializer_class = EmpSerializer

