from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.

def familiares_lista (request):
    familiar_nuevo = Familiares.objects.create (name = 'Irene', last_name = 'Saade', age = '71', gender = 'femenino', relationship = 'madre')
    context = {
        'familiar_nuevo' : familiar_nuevo
    }
    return render (request,'familiar_nuevo.html', context = context)

def familiares_lista2 (request):
    todos_los_familiares = Familiares.objects.all() 
    context = {
        'todos_los_familiares' : todos_los_familiares

    }
        
    return render (request, 'familiares_todos.html', context = context)