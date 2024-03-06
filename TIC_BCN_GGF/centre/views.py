from django.shortcuts import render
from django.template import Context,loader
from django.http import HttpResponse
# Create your views here.
def index(request):
    professor = {"name":"Roger", "surname": "Sobrino", "age":"17"}
    template = loader.get_template('index_centre.html')
    dades = template.render({'nombre': professor["name"], 'surname':professor["surname"], 'age':professor["age"]})
    return HttpResponse(dades)
