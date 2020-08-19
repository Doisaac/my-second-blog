from django.shortcuts import render
from django.views import generic
from .forms import ProductForm
from .models import add
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.
 
class HomeList(generic.ListView):
    imagen = add.objects.all()
    contexto = {'imagen': imagen}
    model = add
    template_name = 'blog/home.html'
    def get_object(self):
         id_ = self.kwargs.get("id")



def product_create_view(request):
    form = ProductForm(request.POST)
    
    if form.is_valid():
        form.save()
    success_url = reverse_lazy('Post:home')    

    context = {
        'form': form
    }
    return render(request, 'crear_form.html', context )