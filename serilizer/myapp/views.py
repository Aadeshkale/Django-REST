from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import  Emp
from myapp.serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class EmpView(APIView):

    def get(self,request):
        allinfo=Emp.objects.all()
        serdinfo=EmpSerializer(allinfo,many=True)
        return Response(serdinfo.data)

