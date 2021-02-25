from django.db import models
from student.models import Student

# Create your models here.


class Course (models.Model):
    name = models.CharField(max_length=200)
    total_marks = models.IntegerField()

    def __str__(self):
        return self.name



class StudentMarks (models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    obtained_marks = models.IntegerField()

    class Meta:
        unique_together = [['student', 'course']]

    def __str__(self):
        return self.course.name
