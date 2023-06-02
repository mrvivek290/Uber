from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import *
from users.serializers import *


class GetStudentsView(APIView):
     
     def get(self,request):
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name :
         instance = Students.objects.filter(first_name = name)
        else:        
         instance = Students.objects.all()
        serializer = StudentsSerializers(instance,many=True)
        return Response(serializer.data)
     
     def post(self,request):
        params = request.data
        print("params",params)
        serializers = StudentsSerializers(data=params)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message":"done"})
     



class GetOrdersView(APIView):
     
     def get(self,request):
        print("req",request.GET)
        ordername = request.GET.get("ordername")
        print("ordername",ordername)
        if ordername :
         instance = Orders.objects.filter(first_name = ordername)
        else:        
         instance = Orders.objects.all()
        serializer = OrdersSerializers(instance,many=True)
        return Response(serializer.data)
     
     def post(self,request):
        params = request.data
        print("params",params)
        serializers = OrdersSerializers(data=params)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message","done"})



class DeleteStudentViews(APIView):
   def get(self,request,pk):
      instance = Students.objects.get(id = pk)
      instance.delete()
      return Response({"message","deletesuccesfully"})

class StudentsDetailAddressViews(APIView):
    def get(self,request,pk):
        instances = Students.objects.filter(id = pk)
        serializer = StudentsDetailAddressSerializers(instances,many = True)
        return Response(serializer.data)
    

class DeleteStudentsAddressViews(APIView):
   def get(self,request,pk):
      instance = Students.objects.get(id = pk)
      addresses = StudentsAddress.objects.filter(students = instance)
      addresses.delete()
      return Response({"message","deletesuccesfully"})

