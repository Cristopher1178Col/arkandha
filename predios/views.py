from django.shortcuts import render, redirect, get_object_or_404
from .models import Predio, Propietario
from .forms import PredioForm, PropietarioForm

# Vista para listar todos los predios
def listar_predios(request):
    predios = Predio.objects.all().prefetch_related('propietarios')  # Optimización para relaciones ManyToMany
    return render(request, 'predios/listar_predios.html', {'predios': predios})

# Vista para crear un nuevo predio
def crear_predio(request):
    if request.method == 'POST':
        form = PredioForm(request.POST)
        if form.is_valid():
            predio = form.save()  # Guardamos el predio creado
            return redirect('listar_predios') 
    else:
        form = PredioForm()
    return render(request, 'predios/crear_predio.html', {'form': form})


# Vista para editar un predio existente
def editar_predio(request, pk):
    predio = get_object_or_404(Predio, pk=pk)
    if request.method == 'POST':
        form = PredioForm(request.POST, instance=predio)
        if form.is_valid():
            form.save()
            return redirect('listar_predios')
    else:
        form = PredioForm(instance=predio)
    return render(request, 'predios/editar_predio.html', {'form': form})

# Vista para eliminar un predio
def eliminar_predio(request, pk):
    predio = get_object_or_404(Predio, pk=pk)
    predio.delete()
    return redirect('listar_predios') 

#Vista para eliminar un propietario

def eliminar_propietario(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    propietario.delete()
    return redirect('listar_todos_propietarios')

# Vista para listar todos los propietarios
def listar_todos_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'predios/listar_todos_propietarios.html', {'propietarios': propietarios})

def listar_propietarios(request):
    propietarios = Propietario.objects.all()  # Trae todos los propietarios
    return render(request, 'propietarios/listar_propietarios.html', {'propietarios': propietarios})

# Vista para listar los propietarios de un predio específico
def listar_propietarios_de_predio(request, pk):
    predio = get_object_or_404(Predio, pk=pk)
    propietarios = predio.propietarios.all()
    return render(request, 'predios/listar_propietarios.html', {'predio': predio, 'propietarios': propietarios})

# Vista para crear un propietario 
def crear_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            propietario = form.save()  # Guarda el nuevo propietario
            return redirect('listar_todos_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'predios/crear_propietario.html', {'form': form})


# Vista para editar un propietario
def editar_propietario(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('listar_todos_propietarios')
    else:
        form = PropietarioForm(instance=propietario)
    
    return render(request, 'predios/editar_propietario.html', {'form': form, 'propietario': propietario})

# Vista Home
def home(request):
    predios = Predio.objects.all()
    return render(request, 'predios/home.html', {'predios': predios})

# Vista para ver los predios de un propietario
def predios_propietario(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    predios = propietario.predio_set.all()  # 'predio_set' es el nombre automático que Django asigna
    return render(request, 'predios/predios_propietario.html', {'propietario' :propietario,'predios': predios})

#Vista para ver los propietarios de un predio
def propietario_predio(request, pk):
    predio = get_object_or_404(Predio,pk=pk)
    propietarios= predio.propietarios.all()
    return render(request, 'predios/propietario_predios.html', {'predio': predio, 'propietarios': propietarios})  # 'propietarios