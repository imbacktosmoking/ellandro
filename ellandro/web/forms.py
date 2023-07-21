from django import forms
from .models import Client 

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client 
        fields = ('author', 'email', 'body', 'date' )

        widgets = {

            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control',}),
            'date':forms.TextInput(attrs={'class': 'form-control', 'type':'hidden' }),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }
