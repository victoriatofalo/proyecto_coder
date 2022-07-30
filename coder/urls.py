from django.urls import path
from coder.views import *

urlpatterns = [ 
    path("",inicio),
    path("cursos/", cursos),
    path("estudiante/",estudiante),
    path("profesor/",profesor),
    path("entregable/",entregable)
]