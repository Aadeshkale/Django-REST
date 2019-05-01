from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authapp.models import Emp
from authapp.serialzers import EmpSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

class Access(APIView):
    authentication_classes = ObtainAuthToken
    permission_classes = IsAuthenticated
    def get(self,request):
        data = Emp.objects.all()
        serialdata = EmpSerializer(data,many=True)
        return Response(serialdata.data)

    def post(self,request):
        data=request.data
        serialdata=EmpSerializer(data=data)
        if serialdata.is_valid():
            serialdata.save()
            return Response({'message':'data stored successfully'},status=200)
        else:
            return Response({'message': 'data is not valid'},status=404)
