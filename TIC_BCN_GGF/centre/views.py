from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
# Create your views here.
def index(request):
   professor = {"name":"Roger","surname":"Sobrino","age":"17"}

   return render(request, 'index_centre.html',{'name':professor["name"],'surname':professor["surname"], 'age':professor["age"]})

def students(request):
   estudiants = [
      {"nom":"Gemma","cognom1":"Garrigosa","cognom2":"Francés","correu":"2023_gemma.garrigosa@iticbcn.cat","curs":"DAW2A","moduls":"M07"},
      {"nom": "Adrià", "cognom1": "Garcia", "cognom2": "Pérez", "correu": "2023_adria.garcia@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Òscar", "cognom1": "Pérez", "cognom2": "Mengual", "correu": "2023_oscar.perez@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Veronica", "cognom1": "Cartagena", "cognom2": "Jaldin", "correu": "2023_veronica.cartagena@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Joana", "cognom1": "Lin", "cognom2": "Chen", "correu": "2023_joana.lin@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Oriana", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Facundo", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Angelo", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Angel", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Eric", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Anxo", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Joel", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Dinar", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Jun", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Jianjing", "cognom1": "Niu", "cognom2": "sensecognom2", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"nom": "Neus", "cognom1": "Garrigosa", "cognom2": "Francés", "correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},

   ]
'''
def teachers(request):
'''