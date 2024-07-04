from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),

    path('Recursos', views.recursos, name='Recursos'),
    path('agregarEmp',views.agregarEmp, name='agregarEmp'),
    path('encontrarEmp/<str:pk>', views.encontrarEmp, name='encontrarEmp'),
    path('deleteEmp/<str:pk>', views.deleteEmp, name='deleteEmp'),
    path('editEmp', views.editEmp, name='editEmp'),

    path('Inventario', views.inventario, name='Inventario'),
    path('agregarInv',views.agregarInv, name='agregarInv'),
    path('deleteProd/<str:pk>',views.deleteProd, name = "deleteProd"),
    path('encontrarProd/<str:pk>', views.encontrarProd, name= "encontrarProd"),
    path('editProd',views.editProd, name="editProd")
]