from django.db import models
'''
se crean las clases de propietario y predio con sus respectivos atributos 

'''
class Propietario(models.Model):
    TIPO_IDENTIFICACION_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('NIT', 'Número de Identificación Tributaria'),
        ('TI', 'Tarjeta de Identidad'),
    ]
    TIPO_PERSONA_CHOICES = [
        ('N', 'Natural'),
        ('J', 'Jurídica'),
    ]

    '''
    models.Charsfield es para definir el campo de texto que ira a la base de datos.
    almacenara cadenas de texto de longitud limitada
    '''

    nombre = models.CharField(max_length=100)
    tipo_persona = models.CharField(max_length=1, choices=TIPO_PERSONA_CHOICES)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    tipo_identificacion = models.CharField(max_length=3, choices=TIPO_IDENTIFICACION_CHOICES)

    def __str__(self):
        return self.nombre

class Predio(models.Model):
    TIPO_PREDIO_CHOICES = [
        ('U', 'Urbano'),
        ('R', 'Rural'),
    ]
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=1, choices=TIPO_PREDIO_CHOICES)
    numero_catastral = models.CharField(max_length=30, unique=True)
    numero_matricula = models.CharField(max_length=50, unique=True)
    propietarios = models.ManyToManyField(Propietario)  # Relación Mnuchosa muchos

    def __str__(self):
        return self.nombre