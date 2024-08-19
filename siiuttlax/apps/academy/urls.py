from django.urls import path
from django.contrib import admin
from django.urls import include

from . import views

app_name = 'academy'
urlpatterns = [
    path('student/create/', views.create_student, name='create_student'),
    path('professor/create/', views.create_professor, name='create_professor')
]
