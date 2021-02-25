from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from .serializer import CourseSerializer
from rest_framework import status

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
