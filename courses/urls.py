from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.Course_list),
    path('studentmarks/', views.student_marks_list),
    path('studentmarks/<int:pk>/', views.Student_Marks_Delete),
]
