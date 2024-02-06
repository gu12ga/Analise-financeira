from django.urls import path
from . import views

urlpatterns = [
    path('insercao/', views.insercao, name='insercao'),
    path('insercao-teste/', views.insercao_teste, name='insercao_teste')
]