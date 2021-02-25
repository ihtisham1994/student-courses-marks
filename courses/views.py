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


@api_view(['GET', 'POST'])
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


@api_view(['DELETE', 'PUT'])
def Student_Marks_Update_Delete( request, pk ):
    if request.method == 'DELETE':
        try:
            studentmark = StudentMarks.objects.get(pk=pk)
            studentmark.delete()
            return Response(status=status.HTTP_200_OK)
        except studentmark.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        try:
            studentmark = StudentMarks.objects.get(pk=pk)
            serializer = StudentMarksSerializer( studentmark, data=request.data );
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except studentmark.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
