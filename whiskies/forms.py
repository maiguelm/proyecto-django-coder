from django import forms

class CrearWhiskyForm(forms.Form):
    etiqueta = forms.CharField(max_length=30)
    aniejamiento = forms.CharField(max_length=30)
    tipo = forms.ChoiceField(choices=[('whisky', 'Whisky'),('bourbon', 'Bourbon'),('otros', 'Otros')])
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))

class BuscarWhisky(forms.Form):
    etiqueta = forms.CharField(max_length=30, required=False)