from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentCreationForm, ProfessorCreationForm

def create_student(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form=StudentCreationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home:home')
    
    return render(request, 'academy/create_student.html', 
                  {'form':form})

def create_professor(request):
    form =ProfessorCreationForm()
    if request.method == 'POST':
        form = ProfessorCreationForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('home:home')
        
    return render(request, 'academy/create_professor.html',
                  {'form':form})