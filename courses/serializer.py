from rest_framework import serializers
from .models import Course, StudentMarks


class CourseSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Course
        fields = ('id', 'name', 'total_marks')


class StudentMarksSerializer ( serializers.ModelSerializer ):
    class Meta: 
        model = StudentMarks
        fields = ('id','student', 'course', 'obtained_marks')
