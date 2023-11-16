from django import forms
from django.contrib.auth.models import User
from mensajes.models import Mensaje

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
    contenido = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí'}))
    
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MensajeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['destinatario'].queryset = User.objects.exclude(pk=user.pk)
