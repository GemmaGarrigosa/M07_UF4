from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('students/', views.students, name="students"),
   path('professors/', views.professors, name="professors"),
   path('students/student/<str:pk>/', views.student,name="student"),
   path('professors/professor/<str:pk>/', views.professor, name="professor"),
   path('delete_usuari/<str:pk>/', views.delete_user, name="eliminar_usuari"),
   path('update_usuari/<str:pk>/', views.update_user, name="editar_usuari"),
   path('formulari/', views.form_user, name="form_user"), # Afegim la ruta que cridarà a la funció form_user a views
]