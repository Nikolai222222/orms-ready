from django.shortcuts import render
from .models import Genero , Cliente

from .forms import GeneroForm

# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    context={"clientes":clientes}
    return render(request,"clientes/index.html",context)

def crud(request):
    clientes = Cliente.objects.all()
    context={"clientes":clientes}
    return render(request,"clientes/clientes_list.html",context)

def clientesAdd(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context={"generos":generos}
        return render(request,"clientes/clientes_add.html",context)
    else:
        generos = Genero.objects.all()        
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj=Cliente.objects.create(
            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = {"mensaje":"Ok , datos guardados.....","generos":generos}
        return render(request,"clientes/clientes_add.html",context)

def clientes_del(request,pk):
    context = {}
    try:
        cliente = Cliente.objects.get(rut=pk)

        cliente.delete()

        mensaje = "Eliminado satisfactoriamente"
        clientes = Cliente.objects.all()
        context = { "clientes": clientes , "mensaje": mensaje }
        return render(request,"clientes/clientes_list.html",context)
    except:
        mensaje = "Error al eliminar"
        clientes = Cliente.objects.all()
        context = {"clientes":clientes,"mensaje":mensaje}
        return render("clientes/clientes_list.html", context)
    
def clientes_findEdit(request,pk):
    if pk != "":
        cliente=Cliente.objects.get(rut=pk)
        #alumno = Alumno.objects.raw(f"SELECT * FROM alumnos_alumno WHERE rut={pk}")
        generos = Genero.objects.all()

        print(type(cliente.id_genero.genero))

        context = {'cliente':cliente,'generos':generos}

        if cliente:
            return render(request,"clientes/clientes_edit.html",context)
        else:
            context={"mensaje":"Error, rut no existe"}
            return render(request,"clientes/clientes_edit.html",context)

def clientesUpdate(request):
    
    if request.method == "POST":
        print("Entra por aqui si es post")
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        objGenero = Genero.objects.get(id_genero = genero)

        cliente = Genero()
        cliente.rut = rut
        cliente.nombre = nombre
        cliente.apellido_paterno = aPaterno
        cliente.apellido_materno = aMaterno
        cliente.fecha_nacimiento = fechaNac
        cliente.id_genero = objGenero
        cliente.telefono = telefono
        cliente.email = email
        cliente.direccion = direccion
        cliente.activo = 1

        cliente.save()

        generos = Genero.objects.all()
        context = {"mensaje":"Datos actualizados satisfactoriamente","generos":generos,"cliente":cliente}
        return render(request, "clientes/clientes_edit.html",context)
    else:
        print("Si no es post")
        #no es un post , entonces se muetra un formulario para hacer un add (insert)
        clientes = Cliente.objects.all()
        context = {"clientes":clientes}
        return render(request,"clientes/clientes_list.html",context)
    

def crud_generos(request):
    generos = Genero.objects.all()
    context = { "generos" : generos }
    return render(request,"generos/generos_list.html",context)

def generosAdd(request):
    context = {}
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid:
            form.save()

            #Limpiar mi formulario
            form = GeneroForm()

            context = {"mensaje":"Genero guardado satisfactoriamente","form":form}
            return render(request,"generos/generos_add.html", context)
    else:
        form = GeneroForm()
        context = {"form":form}
        return render(request,"generos/generos_add.html", context)

def generos_del(request,pk):
    mensajes = [] #En python los arreglos se llaman listas
    errores=[]
    generos = Genero.objects.all()
    try:
        genero = Genero.objects.get(id_genero = pk)
        if genero:
            genero.delete()
            mensajes.append("Bien , genero eliminado satisfactoriamente")
            context = {"generos":generos,"mensajes":mensajes,"errores":errores}
            return render(request,"generos/generos_list.html",context)
    except:
        genero = Genero.objects.all()
        mensaje = "Error , el id no existe para ser eliminado"
        context = {"mensaje":mensaje,"generos":generos}
        return render(request,"generos/generos_list.html",context)
    
def generos_edit(request,pk):
    try:
        genero = Genero.objects.get(id_genero=pk)
        context = {}
        if genero:
            if request.method == "POST":
                form = GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje = "Genero Actualizado Correctamente"
                context = {"genero": genero, "form":form, "mensaje":mensaje}
                return render(request,"generos/generos_edit.html",context)
            else:
                form = GeneroForm(instance=genero)
                mensaje=""
                context = {"genero":genero, "form":form, "mensaje":mensaje}
                return render(request,"generos/generos_edit.html",context)
    except:
        generos = Genero.objects.all()
        mensajes = "Error , el id no existe"
        context = {"mensaje":mensajes,"generos":generos}
        return render(request,"generos/generos_list.html",context)