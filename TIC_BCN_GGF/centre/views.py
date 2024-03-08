from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
# Create your views here.
def index(request):
   professor = {"name":"Roger","surname":"Sobrino","age":"17"}

   return render(request, 'index_centre.html',{'name':professor["name"],'surname':professor["surname"], 'age':professor["age"]})
