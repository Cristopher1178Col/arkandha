from django import forms
from .models import Predio , Propietario

class PredioForm(forms.ModelForm):
    class Meta:
        model = Predio
       # fields = ['nombre', 'tipo', 'numero_catastral', 'numero_matricula', 'propietarios'] # Solo si se quiere mostrar datos especificos
        fields = '__all__' 
        widgets = {
            'numero_catastral': forms.TextInput(attrs={
                'pattern': r'\d{30}',
                'title': '30 dígitos exactos',
                'placeholder': 'Ingrese el número catastral'
            }),
            'propietarios': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),
        }
class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario 
        fields = '__all__' 
        widgets = {
            'numero_identificacion': forms.TextInput(attrs={
                'pattern': r'\d{1,30}',  # Allow 1 to 30 digits
                'title': '1 a 30 dígitos',
                'placeholder': 'Ingrese el número de identificación'
            }),

        }