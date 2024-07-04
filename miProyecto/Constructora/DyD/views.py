from django.shortcuts import render
from .models import Empleado, Producto  
# Create your views here.

def index(request):
    context = {}
    return render(request, 'DyD/index.html',context)

def inicio(request):
    context = {}
    return render(request, 'DyD/inicio.html',context)

def login(request):
    context = {}
    return render(request, 'DyD/login.html',context)

def inventario(request):
    inventario = Producto.objects.all()
    context = {'inventario':inventario}
    return render(request, 'DyD/inventario.html',context)

def agregarInv(request):
    if request.method == 'POST':
        id=request.POST['id_prod']
        nombre=request.POST["nombre_prod"]
        cantidad=request.POST["cantidad_prod"]
        almacenaje=request.POST["formato_prod"]
    obj = Producto.objects.create(
                                    id_prod=id,
                                    nombre_prod=nombre,
                                    cantidad_prod=cantidad,
                                    almacenaje=almacenaje
                                )
    obj.save()
    context= {'mensaje': "Agregado con exito"}
    return render(request,'DyD/inventario.html',context)

def deleteProd(request, pk):
    context={}
    try:
        producto = Producto.objects.get(id_prod=pk)
        producto.delete()
        mensaje= "Datos eliminados"
        productos= Producto.objects.all()
        context={'inventario':productos, 'mensaje': mensaje}
        return render(request, 'DyD/inventario.html', context)
    except:
        mensaje= "Id no encontrado"
        productos= Producto.objects.all()
        context={'inventario':productos, 'mensaje': mensaje}
        return render(request, 'DyD/inventario.html', context)

def encontrarProd(request,pk):
    if pk != "":
        producto= Producto.objects.get(id_prod=pk)

        context={'producto':producto}
        if producto:
            return render(request, 'DyD/editarInv.html', context)
        else:
            context={'mensaje':"Error, rut no existe"}
            return render(request, 'DyD/editarInv.html', context)
        
def editProd(request):
    if request.method == "POST":
        id=request.POST['id_prod']
        nombre=request.POST["nombre_prod"]
        cantidad=request.POST["cantidad_prod"]
        almacenaje=request.POST["formato"]

        prod = Producto()

        prod.id_prod=id
        prod.nombre_prod=nombre
        prod.cantidad_prod=cantidad
        prod.almacenaje=almacenaje
        prod.save()

        context={'mensaje': "Datos actualizados correctamente", 'producto':prod}
        return render(request, 'DyD/recursos.html', context)
    else:
        #not post
        prod = Producto.objects.all()
        context={'producto':prod}
        return render(request, 'DyD/recursos.html', context)
    

#########################################################################333
def recursos(request):
    personal = Empleado.objects.all()
    context = {'personal': personal}
    return render(request, 'DyD/recursos.html',context)

def agregarEmp(request):
    if request.method == 'POST':
        rut=request.POST["rut"]
        nombre=request.POST["nombre_emp"]
        sueldo=request.POST["sueldo"]
        email=request.POST["email"]
        activo="1"
    obj = Empleado.objects.create(
                                    rut=rut,
                                    nombre=nombre,
                                    sueldo=sueldo,
                                    email=email,
                                    activo=activo
                                )
    obj.save()
    context= {'mensaje': "Agregado con exito"}
    return render(request,'DyD/recursos.html',context)

def deleteEmp(request, pk):
    context={}
    try:
        persona = Empleado.objects.get(rut=pk)
        persona.delete()
        mensaje= "Datos eliminados"
        personas= Empleado.objects.all()
        context={'personal':personas, 'mensaje': mensaje}
        return render(request, 'DyD/recursos.html', context)
    except:
        mensaje= "Rut no encontrado"
        personas= Empleado.objects.all()
        context={'personal':personas, 'mensaje': mensaje}
        return render(request, 'DyD/recursos.html', context)
    
def encontrarEmp(request,pk):
    if pk != "":
        persona= Empleado.objects.get(rut=pk)

        context={'empleado':persona}
        if persona:
            return render(request, 'DyD/editarEmp.html', context)
        else:
            context={'mensaje':"Error, rut no existe"}
            return render(request, 'DyD/editarEmp.html', context)
        
def editEmp(request):
    if request.method == "POST":
        rut=request.POST['rut']
        nombre=request.POST['nombre']
        sueldo=request.POST['sueldo']
        email=request.POST['email']
        activo="1"

        emp = Empleado()

        emp.rut=rut
        emp.nombre=nombre
        emp.sueldo=sueldo
        emp.email=email
        emp.activo=activo
        emp.save()

        context={'mensaje': "Datos actualizados correctamente", 'empleado':emp}
        return render(request, 'DyD/recursos.html', context)
    else:
        #not post
        personal = Empleado.objects.all()
        context={'personal':personal}
        return render(request, 'DyD/recursos.html', context)
    
