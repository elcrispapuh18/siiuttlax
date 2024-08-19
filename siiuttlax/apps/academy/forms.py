from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Professor

class StudentCreationForm(UserCreationForm):

 class Meta:
    model = Student
    fields = ['username', 'email', 
              'first_name', 'enrollment', 'password1', 'password2']

class ProfessorCreationForm(UserCreationForm):
  class Meta:
    model = Professor
    fields = ['username', 'email', 'first_name', 'password1', 'password2', 'employee_number']