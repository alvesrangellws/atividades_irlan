from django import forms
from django.core.exceptions import ValidationError

class produtoForm(forms.Form):
    nome = forms.ChoiceField(label="nao pode ter menos de 3 letras")