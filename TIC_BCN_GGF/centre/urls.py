from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('students/', views.students, name="students"),
   path('professors/', views.professors, name="professors"),
   path('students/student/<str:pk>/', views.student,name="student"),
   path('professors/professor/<str:pk>/', views.professor, name="professor")
]