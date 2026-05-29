from django.shortcuts import render, HttpResponse
from .models import TODOItem

# Create your views here.
def home(request):
    return render(request, 'db_app/home.html')

def about(request):
    return render(request, 'about.html')

def todos(request):
    items = TODOItem.objects.all()
    return render(request, 'todos.html', {'todos': items})