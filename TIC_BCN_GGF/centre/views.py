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
   profes = User.objects.get(attribute=pk)
   profes_Obj = None
   for i in profes :
      if i['id']==pk:
         profes_Obj = i
   return render(request, 'professor.html',{"professor":profes_Obj})
def student (request, pk):
   estudiants = User.objects.all() #esta malament aixo
   students_Obj = None
   for i in estudiants:
      if i['id']== pk:
         students_Obj = i
   return render(request, 'student.html',{"student":students_Obj})

def form_user(request):
   form = UserForm()
   context = {'form':form}
   return render(request, 'formulari_users.html',context)


