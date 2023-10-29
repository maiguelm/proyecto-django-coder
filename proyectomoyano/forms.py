from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    mail = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    consulta = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))
    
class CrearVinoForm(forms.Form):
    etiqueta = forms.CharField(max_length=30)
    varietal = forms.CharField(max_length=30)
    cosecha = forms.IntegerField()
    tipo = forms.ChoiceField(choices=[('vino_tinto', 'Vino Tinto'),('vino_blanco', 'Vino Blanco'),('vino_rosado', 'Vino Rosado')])
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))
    
class CrearWhiskyForm(forms.Form):
    etiqueta = forms.CharField(max_length=30)
    aniejamiento = forms.CharField(max_length=30)
    tipo = forms.ChoiceField(choices=[('whisky', 'Whisky'),('bourbon', 'Bourbon'),('otros', 'Otros')])
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))

class BuscarVino(forms.Form):
    etiqueta = forms.CharField(max_length=30, required=False)

class BuscarWhisky(forms.Form):
    etiqueta = forms.CharField(max_length=30, required=False)