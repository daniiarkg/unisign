from django.forms import ModelForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError


class PetitionSearchForm(forms.Form):
    title = forms.CharField(label='Поиск петиций', max_length=60)
