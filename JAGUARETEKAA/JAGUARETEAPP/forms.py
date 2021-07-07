from .models import Producto
from django import forms


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('categoria', 'nombre', 'descripcion', 'precio', 'imagen', 'fecha')
        widgets = {
            'categoria': forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "categoria",
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            'fecha': forms.SelectDateWidget(
                attrs={
                    "class": "visually-hidden",
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    "class": "form-control",
                    
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    "class": "form-control",
                   
                }
            ),
            'imagen': forms.ClearableFileInput(),
    
        }