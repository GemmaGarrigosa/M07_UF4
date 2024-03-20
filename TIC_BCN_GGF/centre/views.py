from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.
def index(request):
   professor = {"name":"Roger","surname":"Sobrino","age":"17"}

   return render(request, 'index_centre.html',{'name':professor["name"],'surname':professor["surname"], 'age':professor["age"]})

def students(request):
   estudiants = [ #Guardem en un array la llista d'alumnes
      {"id": 1, "nom":"Gemma","cognom1":"Garrigosa","cognom2":"Francés","correu":"2023_gemma.garrigosa@iticbcn.cat","curs":"DAW2A","moduls":"M07"},
      {"id": 2,"nom": "Adrià", "cognom1": "Garcia", "cognom2": "Pérez", "correu": "2023_adria.garcia@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 3,"nom": "Òscar", "cognom1": "Pérez", "cognom2": "Mengual", "correu": "2023_oscar.perez@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 4,"nom": "Veronica", "cognom1": "Cartagena", "cognom2": "Jaldin", "correu": "2023_veronica.cartagena@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 5,"nom": "Joana", "cognom1": "Lin", "cognom2": "Chen", "correu": "2023_joana.lin@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 6,"nom": "Oriana Saray", "cognom1": "Rojas", "cognom2": "Guedez", "correu": "2023_oriana.rojas@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 7,"nom": "Facundo Calixto", "cognom1": "Barrios", "cognom2": "", "correu": "2023_facundo.barrios@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 8,"nom": "Angelo", "cognom1": "Montenegro", "cognom2": "Zavala", "correu": "2023_angelo.montenegro@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 9,"nom": "Angel", "cognom1": "Ivanov", "cognom2": "Spasov", "correu": "2023_angel.ivanov@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 10,"nom": "Eric", "cognom1": "Sanchez", "cognom2": "Vazquez", "correu": "2023_eric.sanchez@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 11,"nom": "Anxo", "cognom1": "Aragundi", "cognom2": "Mesias", "correu": "2023_anxo.aragundi@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 12,"nom": "Joel", "cognom1": "Ghanem", "cognom2": "Gomez", "correu": "2023_joel.ghanem@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 13,"nom": "Dinar", "cognom1": "Khazimullin", "cognom2": "", "correu": "2023_dinar.khazimullin@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 14,"nom": "JunHong", "cognom1": "Zhu", "cognom2": "Zhang", "correu": "2023_junhong.zhu@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 15,"nom": "Jianjing", "cognom1": "Niu", "cognom2": "", "correu": "2023_jianjing.niu@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 16,"nom": "Neus", "cognom1": "Bravo", "cognom2": "Arias", "correu": "2023_neus.bravo@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},

   ]
   return render(request,'students.html',{"students":estudiants}) #envia al html el objecte students que conté l'array d'estudiants

def professors(request):
   profes = [
      {"id": 1,"nom":"Roger","cognom1":"Sobrino","cognom2":"Gil","correu":"roger.sobrino@iticbcn.cat","tutor":"NO","curs":"DAW2A","moduls":"M07"},
      {"id": 2,"nom": "Juan Manuel", "cognom1": "Sanchez", "cognom2": "Bel", "correu": "juanmanuel.sanchez@iticbcn.cat","tutor":"SI", "curs": "DAW2A", "moduls": "M06"},
      {"id": 3,"nom": "Josep Oriol", "cognom1": "Roca", "cognom2": "Fabra", "correu": "joseporiol.roca@iticbcn.cat","tutor":"NO", "curs": "DAW2A", "moduls": "M09"},
      {"id": 4,"nom": "Xavi", "cognom1": "Quesada", "cognom2": "Puertas", "correu": "xavi.quesada@iticbcn.cat","tutor":"NO", "curs": "DAW2A", "moduls": "M08/M013"},

   ]
   return render(request,'professors.html',{"professors":profes})

def professor(request, pk):
   profes = [
      {"id": 1, "nom": "Roger", "cognom1": "Sobrino", "cognom2": "Gil", "correu": "roger.sobrino@iticbcn.cat","tutor": "NO", "curs": "DAW2A", "moduls": "M07"},
      {"id": 2, "nom": "Juan Manuel", "cognom1": "Sanchez", "cognom2": "Bel","correu": "juanmanuel.sanchez@iticbcn.cat", "tutor": "SI", "curs": "DAW2A", "moduls": "M06"},
      {"id": 3, "nom": "Josep Oriol", "cognom1": "Roca", "cognom2": "Fabra", "correu": "joseporiol.roca@iticbcn.cat","tutor": "NO", "curs": "DAW2A", "moduls": "M09"},
      {"id": 4, "nom": "Xavi", "cognom1": "Quesada", "cognom2": "Puertas", "correu": "xavi.quesada@iticbcn.cat","tutor": "NO", "curs": "DAW2A", "moduls": "M08/M013"},
   ]
   profes_Obj = None
   for i in profes :
      if i['id']==pk:
         profes_Obj = i
   return render(request, 'professor.html',{"professor":profes_Obj})
def student (request, pk):
   estudiants = [  # Guardem en un array la llista d'alumnes
      {"id": 1, "nom": "Gemma", "cognom1": "Garrigosa", "cognom2": "Francés","correu": "2023_gemma.garrigosa@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 2, "nom": "Adrià", "cognom1": "Garcia", "cognom2": "Pérez", "correu": "2023_adria.garcia@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 3, "nom": "Òscar", "cognom1": "Pérez", "cognom2": "Mengual", "correu": "2023_oscar.perez@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 4, "nom": "Veronica", "cognom1": "Cartagena", "cognom2": "Jaldin","correu": "2023_veronica.cartagena@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 5, "nom": "Joana", "cognom1": "Lin", "cognom2": "Chen", "correu": "2023_joana.lin@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 6, "nom": "Oriana Saray", "cognom1": "Rojas", "cognom2": "Guedez","correu": "2023_oriana.rojas@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 7, "nom": "Facundo Calixto", "cognom1": "Barrios", "cognom2": "","correu": "2023_facundo.barrios@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 8, "nom": "Angelo", "cognom1": "Montenegro", "cognom2": "Zavala","correu": "2023_angelo.montenegro@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 9, "nom": "Angel", "cognom1": "Ivanov", "cognom2": "Spasov", "correu": "2023_angel.ivanov@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 10, "nom": "Eric", "cognom1": "Sanchez", "cognom2": "Vazquez", "correu": "2023_eric.sanchez@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 11, "nom": "Anxo", "cognom1": "Aragundi", "cognom2": "Mesias", "correu": "2023_anxo.aragundi@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 12, "nom": "Joel", "cognom1": "Ghanem", "cognom2": "Gomez", "correu": "2023_joel.ghanem@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 13, "nom": "Dinar", "cognom1": "Khazimullin", "cognom2": "","correu": "2023_dinar.khazimullin@iticbcn.cat", "curs": "DAW2A", "moduls": "M07"},
      {"id": 14, "nom": "JunHong", "cognom1": "Zhu", "cognom2": "Zhang", "correu": "2023_junhong.zhu@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 15, "nom": "Jianjing", "cognom1": "Niu", "cognom2": "", "correu": "2023_jianjing.niu@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
      {"id": 16, "nom": "Neus", "cognom1": "Bravo", "cognom2": "Arias", "correu": "2023_neus.bravo@iticbcn.cat","curs": "DAW2A", "moduls": "M07"},
   ]
   students_Obj = None
   for i in estudiants:
      if i['id']== pk:
         students_Obj = i
   return render(request, 'student.html',{"student":students_Obj})

def form_user(request):
   form = UserForm()
   context = {'form':form}
   return render(request, 'formulari_users.html',context)