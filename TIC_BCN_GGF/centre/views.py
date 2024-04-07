from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import UserForm
from .models import User

# Create your views here.
def index(request):
   professor = {"name":"Roger","surname":"Sobrino","age":"17"}

   return render(request, 'index_centre.html',{'name':professor["name"],'surname':professor["surname"], 'age':professor["age"]})

def students(request):
   estudiants = User.objects.filter(rol='Alumnat')
   return render(request,'students.html',{'students':estudiants})
   #Guardem en un array la llista d'alumnes



def professors(request):
   profes= User.objects.filter(rol='Professorat')

   return render(request,'professors.html',{"professors":profes})

def professor(request, pk):
   profes = User.objects.get(id=pk)

   return render(request, 'professor.html',{"professor":profes})
def student (request, pk):
   estudiants = User.objects.get(id=pk) #esta malament aixo

   return render(request, 'student.html',{"student":estudiants})


def form_user(request):
   form = UserForm()
   if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
         form.save()
         if form["rol"].value() == "Alumnat":
            return redirect('students')
         else:
            return redirect('professors')
   context = {'form': form}
   return render(request, 'formulari_users.html', context)

def delete_user(request,pk):
   form = User.objects.get(id=pk)
   if request.method == 'POST':
      form.delete()
      if form.rol == "Alumnat":
         return redirect('students')
      else:
         return redirect('professors')
   context = {'form':form}
   return render(request,'delete_users.html',context)

def update_user(request,pk):
   user = User.objects.get(id=pk)
   form = UserForm(instance=user)

   if request.method == 'POST':
      form = UserForm(request.POST, instance=user)
      if form.is_valid():
         form.save()
         if form["rol"].value() == "Alumnat":
            return redirect('students')
         else:
            return redirect('professors')
   context = {'form':form}
   return render(request,'formulari_users.html',context)
