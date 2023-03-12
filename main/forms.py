from django.forms import ModelForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    phone = forms.CharField(
        label='Номер телефона(в формате 996...)', max_length=12)
    password = forms.CharField(
        label='Пароль', max_length=40, widget=forms.PasswordInput)

    def clean(self):
        cl_data = super().clean()
        try:
            c = Citizen.objects.get(phone=cl_data.get('phone'))
            if not check_password(cl_data.get('password'), c.user.password):
                raise ValidationError('Неправильный пароль или номер телефона')
        except:
            raise ValidationError('Неправильный номер телефона')


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=30)
    last_name = forms.CharField(label='Фамилия', max_length=40)
    pin = forms.CharField(label='ПИН', max_length=14)
    phone = forms.CharField(
        label='Номер телефона(в формате 996...)', max_length=12)
    password = forms.CharField(
        label='Пароль', max_length=40, widget=forms.PasswordInput)
    password_val = forms.CharField(
        label='Пароль', max_length=40, widget=forms.PasswordInput)


class PetitionForm(ModelForm):
    class Meta:
        model = Petition
        fields = ['image', 'title', 'text']


class PetitionSearchForm(forms.Form):
    title = forms.CharField(label='Поиск петиций', max_length=60)
