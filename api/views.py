from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class Student_API(APIView):

    def get(self,request,pk=None,format = None):
        id=pk
        if id is not None:
            stu = Student.objects.get(id = id)
            ser = StudentSerializers(stu)
            return Response(ser.data)
        stuList = Student.objects.all()
        ser = StudentSerializers(stuList,many = True)
        return Response(ser.data)
    
    def post(self,request,format = None):
        data =  StudentSerializers(data = request.data)
        if data.is_valid():
            data.save()
            return Response({"msg":"created SuccessFully"},status=status.HTTP_201_CREATED)
        return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format = None):
        id = pk
        stu = Student.objects.get(id = id)
        ser = StudentSerializers(instance=stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"full updated SuccessFully"},status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format = None):
        id = pk
        stu = Student.objects.get(id = id)
        ser = StudentSerializers(instance=stu,data=request.data,partial = True)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Partial updated SuccessFully"},status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk,format = None):
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({"msg":"deleted successfully"},status=status.HTTP_202_ACCEPTED)



