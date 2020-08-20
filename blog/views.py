from django.shortcuts import render
from django.views import generic
from .models import add
from django.views.generic import ListView


# Create your views here.
 
class HomeList(generic.ListView):
    imagen = add.objects.all()
    contexto = {'imagen': imagen}
    model = add
    template_name = 'blog/home.html'
    def get_object(self):
         id_ = self.kwargs.get("id")



