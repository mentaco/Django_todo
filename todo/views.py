from django.shortcuts import render
from django.views.generic import ListView

from .models import Todo

# Create your views here.
class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"