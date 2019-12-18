from django.contrib import admin
from django.urls import path,include
from .views import index,gale,formulario,quie,log,login_acceso,cerrar_sesion,eliminar_flor,registro,carro,graba_carro_compra,Carro_Compra,carro_compra_mas,carro_compra_meno,guardar_token,formulario_api,listar_florAPI,Eliminar_florAPI,guarda_formulario
# se importa FlorviewSet y UserviewSet
 #from rest_framework import 

 #router = routers.DefaultRouter()
 #router.register('Flores',FlorviewSet)
 #router.register('Usuario',UserviewSet)

urlpatterns = [
    path('', index,name='IND'),
    path('galeria/',gale,name="GAL"),
    path('formulario/',formulario,name='FORMU'),
    path('quienes somos',quie,name='QUIEN'),
    path('login/',log,name='LOGIN'),
    path('Login_acceso/',login_acceso,name='LOGINACCESO'),
    path('cerrar_sesion/',cerrar_sesion,name='CERRAR'),
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINO'),
    path('Registro_usuario/',registro,name="REGI"),
    path('Carro_Compra/<id>/',Carro_Compra,name='Agregar_carrito'),    
    path('carro/',carro,name='Carrito'),
    path('carro_mas/<id>/',carro_compra_mas,name='Carro_Mas'),
    path('carro_meno/<id>/',carro_compra_meno,name='Carrro_meno'),
    path('grabar_carro_compra/',graba_carro_compra,name='grabar_carro_compra'),
    path('guardar-token/',guardar_token,name='guardar_token'),
    path('formulario_api/',formulario_api,name='FormularioAPI'),
    path('listar_florAPI/',listar_florAPI,name='LSFAPI'),
    path('Eliminar_florAPI/',Eliminar_florAPI,name='ELIMINAapi'),
    path('guarda_formulario/',guarda_formulario,name='GUARDA_FORMU'),

    #path('api/',include(router.urls)),
    

   
]