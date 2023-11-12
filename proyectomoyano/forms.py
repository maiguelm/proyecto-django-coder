from django import forms
from ckeditor.fields import RichTextFormField

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    mail = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    consulta = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))
    
class CrearVinoForm(forms.Form):
    etiqueta = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ingrese la etiqueta'}))
    varietal = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ingrese el varietal'}))
    cosecha = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese el año'}))
    tipo = forms.ChoiceField(choices=[('vino_tinto', 'Vino Tinto'),('vino_blanco', 'Vino Blanco'),('vino_rosado', 'Vino Rosado')])
    descripcion = RichTextFormField()
    imagen = forms.ImageField(label= 'Imagen del vino', required=False)
    fecha_compra = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    
class BuscarVino(forms.Form):
    etiqueta = forms.CharField(max_length=30, required=False)

