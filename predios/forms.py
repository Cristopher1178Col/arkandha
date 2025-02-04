from django import forms
from .models import Predio, Propietario

class PredioForm(forms.ModelForm):
    class Meta:
        model = Predio
        fields = '__all__'
        widgets = {
            'numero_catastral': forms.TextInput(attrs={
                'pattern': r'\d{30}',
                'title': '30 dígitos exactos',
                'placeholder': 'Ingrese el número catastral'
            }),
            'propietarios': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),
        }
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        qs = Predio.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
           qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
           raise forms.ValidationError('El nombre del predio ya existe.')
        return nombre

    

    def clean_numero_catastral(self):
        numero_catastral = self.cleaned_data.get('numero_catastral')
        qs = Predio.objects.filter(numero_catastral=numero_catastral)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Este número catastral ya está registrado.")
        return numero_catastral

    def clean_numero_matricula(self):
        numero_matricula = self.cleaned_data.get('numero_matricula')
        qs = Predio.objects.filter(numero_matricula=numero_matricula)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Este número de matrícula ya está registrado.")
        return numero_matricula


class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
        widgets = {
            'numero_identificacion': forms.TextInput(attrs={
                'pattern': r'\d{1,30}',  # Permite de 1 a 30 dígitos
                'title': '1 a 30 dígitos',
                'placeholder': 'Ingrese el número de identificación'
            }),
        }
    
    def clean_numero_identificacion(self):
        numero_identificacion = self.cleaned_data.get('numero_identificacion')
        qs = Propietario.objects.filter(numero_identificacion=numero_identificacion)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Este número de identificación ya está registrado.")
        return numero_identificacion
