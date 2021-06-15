from django.shortcuts import render

from .models import Cliente
from .forms import ClienteForm


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form})
