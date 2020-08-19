from django import forms

from .models import add

class ProductForm(forms.ModelForm):
    class Meta:
        model = add 
        fields = [
            'nombre',
            
            


      ]