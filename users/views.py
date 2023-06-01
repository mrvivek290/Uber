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
        if name:
            instance = Students.objects.filter(first_name = name)
        else:
         instance = Students.objects.all()
        serializers = Studentsserializers(instance,many=True)
        return Response (serializers.data)
    def post(self,request):
       
       params = request.data
       print("params",params)

       serializers = Studentsserializers(data=params)
       serializers.is_valid(raise_exception=True)
       serializers.save()

       return Response({"messege","Done"})
    

class GetOrdersViews(APIView):
    def get(self,request):
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name:
            instance = Orders.objects.filter(first_name = name)
        else:
            instance = Orders.objects.all()
        serializers = OrdersSerializers(instance,many=True)
        return Response (serializers.data)
    

    def post(self,request):
       
        param = request.data
        print("params--------",param)

        serializers = Orders(data=param)
        if serializers.is_valid():
           serializers.save()
           return Response({"Order","Placed"})
        else:
           print("error",serializers.errors)
           return Response({"errors":str(serializers.errors)})
    
    

class DeleteStudentsView(APIView):
     def get(self,request,pk):
        instance = Students.objects.get(id=pk)
        instance.delete()
        return Response({"data","deleted"})
     

class StudentsDetailAddressViews(APIView):
    def get(self,request,pk):
        instances = Students.objects.filter(id=pk)
        serializer = StudentsDetailAddressSerializers(instances,many=True)
        return Response(serializer.data)
    


class StudentsAdressDeleteViews(APIView):
    def get(self,request,pk):
        instance = Students.objects.get(id=pk)
        instance = StudentsAdress.objects.filter(students=instance)
        adress.deleted()

        return Response(serializers.data)
         
