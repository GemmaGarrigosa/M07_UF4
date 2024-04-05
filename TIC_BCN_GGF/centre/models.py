from django.db import models

# Create your models here.
# Aqui les taules que hi haurà a la nostra base de dades que necessitarem a la nostra aplicació
# El id es crea automàticament pel framework

class User(models.Model):


    ROLS = [ #Creo una tupla amb clau valor per als dos tipus de rols que existeixen
        ('Alumnat','Alumnat'),
        ('Professorat','Professorat')
    ]
    nom = models.CharField(max_length=50)
    cognom1 = models.CharField(max_length=50)
    cognom2 = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    curs = models.CharField(max_length=50)
    rol = models.CharField(max_length=20, choices=ROLS)
