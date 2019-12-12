from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from .models import Categoria,Flor,Ticket
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .clase import objeto
from .forms import CustinUserForm


# Create your views here.
#def agregar_carrito(request,id):
#    lista=request.session.get("carrito","")
#    lista=lista+str(id)+str(";")
#    request.session["carrito"]=lista
#    return render(request,"core/carrito_compras.html",{'listaCarrito':lista})

# sirve para elmiminar las flores de la bases ded datos
def eliminar_flor(request,id):
    flo=Flor.objects.get(name=id)
    msg=''
    try:
        flo.delete()
        msg='elimino flor'
    except:
        msg='no Elimino'
    lflor=Flor.objects.all()
    return render(request,"core/galeria.html",{'lista':lflor,'msg':msg})

# es una ventata  para ejecutar el login    
def log(request):
    return render(request,"core/login.html")
# sirve para cerrar sessión del usuario    
def cerrar_sesion(request):
    logout(request)
    return render(request,"core/login.html",{'msg':'cerro sesion'})                    

# sirve para que el usuario acceda por medio del login    
def login_acceso(request):
    if request.POST:
        usuario=request.POST.get("txtUser")
        password=request.POST.get("txtPass")
        us= authenticate(request,username=usuario,password=password)    
        request.session["carrito"]=[]
        request.session["carritoC"]=[]
        print('Realizado')
        if us is not None and us.is_active:
            auth_login(request,us)
            return render(request,"core/index.html")
    return render(request,"core/login.html",{'msg':'vuelve ingresar los datos'})

# sirve para abrir la ventata del carrito     
@login_required(login_url='/login/')    
def carro(request):
    x=request.session["carritoC"]
    suma=0
    for item in x:
        suma=suma+int(item["total"])
    return render(request,'core/carrito_compras.html',{'x':x,'total':suma})
# sirve cuando se selecciona el producto
@login_required(login_url='/login/')
def graba_carro_compra(request):
    x=request.session["carritoC"]
    usuario=request.User.username
    suma=0
    try:
        for item in x:
            nombre=item["nombre"]            
            precio=int(item["precio"])
            cantidad=int(item["cantidad"])
            total=int(item["total"])
            ticket=ticket(
                usuario=usuario,
                nombre=nombre,
                precio=precio,
                cantidad=cantidad,
                total=total,
                fecha=dadtetime.date.today()
            )
            ticket.save()
            suma=suma+int(total)
            print("regi grabado")
        mensaje="Grabado en el carrito"
        request.session["carritoC"]=[]
    except:
        mensaje="Error al grabar al carro"
    return  render(request,'core/carro.html',{'x':x,'total':suma,'mensaje':mensaje})                  

# sirve cuando se selecciona un producto, se le agrega como lista en el carrito de compras    
@login_required(login_url='/login/')    
def Carro_Compra(request,id):
    p=Flor.objects.get(name=id)
    x=request.session["carritoC"]
    obj=objeto(1,p.name,p.precio,1)
    sw=0
    suma=0
    clon=[]    
    for item in x:
        cantidad=item["cantidad"]
        if item["nombre"]==p.name:
            sw=1
            cantidad=int(cantidad)+1
        ne=objeto(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    if sw==0:
        clon.append(obj.toString())    
    x=clon
    request.session["carritoC"]=x
    flo=Flor.objects.all()
    return render(request,'core/galeria.html',{'lista':flo,'total':suma})    
# este método aumenta la cantidad de flores selccionada
@login_required(login_url='/login/')    
def carro_compra_mas(request,id):
    f=Flor.objects.get(name=id)
    x=request.session["carritoC"]
    suma=0
    clon=[]
    for item in x:
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
           cantidad=int(cantidad)+1
        ne=objeto(1,item["nombre"],item["precio"],cantidad)
        suma=suma+int(ne.total()) # se calcula la cantidad de flores agregadas por medio de la suma
        clon.append(ne.toString())
    x=clon
    request.session["carritoC"]=x
    x=request.session["carritoC"]
    return render(request,'core/carrito_compras.html',{'x':x,'total':suma})  
# este metodo funciona de la misma manera que en el anterior solamente lo disminuye
@login_required(login_url='/login/')    
def carro_compra_meno(request,id):
    f=Flor.objects.get(name=id)
    x=request.session["carritoC"]
    clon=[]
    suma=0
    for item in x:
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:        
          cantidad=int(cantidad)-1
        ne=objeto(1,item["nombre"],item["precio"],cantidad)    
        suma=suma+int(ne.toString())
    x=clon
    request.session["carritoC"]=x
    return render(request,'core/carrito_compras.html',{'x':x,'total':suma})

# para abrir la ventana principal
@login_required(login_url='/login/')    
def index(request):
    return render(request,'core/index.html')
# para abrir la ventana de la galeria    
@login_required(login_url='/login/')    
def gale(request):
    flo=Flor.objects.all() #se carga las flores desde la base de datos
    return render(request,'core/galeria.html',{'lista':flo})

# formulario para agregar, actualizar y eliminar la flor de la base de datos    
@login_required(login_url='/login/')
def formulario(request):
    categorias=Categoria.objects.all()
    if request.POST:
        accion=request.POST.get("accion")
        if accion=='grabar':
            nombre=request.POST.get("txtNombre")
            valor=request.POST.get("txtValor")
            descripc=request.POST.get("txtDescripcion")
            image=request.FILES.get("txtImagen")
            catego=request.POST.get("cboCategoria")
            obj_categoria=Categoria.objects.get(name=catego)
            estad=request.POST.get("txtestado")
            stoc=request.POST.get("txtStock")
            
            print(estad)

            flo=Flor(
                name=nombre,
                valor=valor,
                descripcion=descripc,
                imagen=image,
                categoria=obj_categoria,
                Estado=estad,
                stock=stoc
            )
            flo.save()
            return render(request,'core/formulario.html',{'listacategoria':categorias,'msg':'guardo flor'})
        if accion=='eliminar':
            nombre=request.POST.get("txtNombre")
            flo=Flor.objects.get(name=nombre)
            flo.delete()
            return render(request,'core/formulario.html',{'listacategoria':categorias,'msg':'elimino'})
    return render(request,'core/formulario.html',{'listacategoria':categorias})


# se abre la ventana de quienes somos
@login_required(login_url='/login/')
def quie(request):
    return render(request,'core/Quienes somos.html') 

# sirve para registar nuevos usuarios por medio de la ventana de registrar usuario
def registro(request):
    data={
        'form':CustinUserForm()
    }
    if request.method=='POST':
        formulario=CustinUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            us=authenticate(username=username,password=password)            
            return redirect(to='IND')
    return render(request,'core/Registro_usuario.html',data)
def isset(variable):
    return variable in locals() or variable in globals()        