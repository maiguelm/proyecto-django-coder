from django import forms

class CrearWhiskyForm(forms.Form):
    etiqueta = forms.CharField(max_length=30)
    aniejamiento = forms.CharField(max_length=30)
    tipo = forms.ChoiceField(choices=[('whisky', 'Whisky'),('bourbon', 'Bourbon'),('otros', 'Otros')])
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))
    imagen = forms.ImageField(label= 'Imagen del vino', required=False)
    fecha_compra = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date'}))

class BuscarWhisky(forms.Form):
    etiqueta = forms.CharField(max_length=30, required=False)