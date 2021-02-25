from django.db import models

# Create your models here.


class Course (models.Model):
    name = models.CharField(max_length=200)
    total_marks = models.IntegerField()

    def __str__(self):
        return self.name
