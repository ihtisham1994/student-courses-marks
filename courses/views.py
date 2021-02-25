from django.shortcuts import render

# from rest_framework import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, StudentMarks
from .serializer import CourseSerializer, StudentMarksSerializer
from rest_framework import status

from rest_framework import viewsets

@api_view(['GET', 'POST'])
def Course_list (request ):
    if request.method == 'GET':
        obj = Course.objects.all()
        serializer = CourseSerializer (obj, many = True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT'])
def student_marks_list ( request ):
    if request.method == 'GET':
        obj = StudentMarks.objects.all()
        serializer = StudentMarksSerializer( obj, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentMarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = StudentMarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StudentMarkDelete(APIView):
#     def delete(request, id=None):
#         return Response({"message": 'hello there'})

@api_view(['DELETE'])
def Student_Marks_Delete( request, pk ):
    if request.method == 'DELETE':
        try:
            print("hello")
            studentmark = StudentMarks.objects.get(pk=pk)
            studentmark.delete()
            return Response(status=status.HTTP_200_SUCCESS)
        except studentmark.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def Student_Marks_Update( request, pk ):
#     if request.method == 'PUT':
#         try:
#             studentmark = StudentMarks.objects.get(pk=pk)
#             studentmark.delete()
#             return Response(status=status.HTTP_200_SUCCESS)
#         except studentmark.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
