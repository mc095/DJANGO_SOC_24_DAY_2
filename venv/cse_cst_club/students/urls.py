from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('hello/', views.hello, name='hello'),
    path('svec/', views.svec, name="svec"),
    path('courses/', views.courses, name="courses"),
    path('stdetails/', views.student_details, name="student_details"),
]