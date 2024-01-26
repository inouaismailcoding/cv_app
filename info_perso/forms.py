from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class ProfileImgForm(forms.ModelForm):
    class Meta:
        model = ProfileImg
        fields = ['photo']
        labels = {
            'photo': _('Photo de profil'),
        }
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class ProfileTextForm(forms.ModelForm):
    class meta:
        model=ProfileTitle
        fields = '__all__'
        
        


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = '__all__'


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('titre', 'entreprise', 'ville', 'debut', 'fin', 'description')

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileTitle
        fields = '__all__'

class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competences
        fields = '__all__'


class LangueForm(forms.ModelForm):
    class Meta:
        model = Langue
        fields = ['langue', 'niveau']

        widgets = {
            'langue': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
        }

class CentreInteretForm(forms.ModelForm):
    class Meta:
        model = CentreInteret
        fields = ['titre']

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
        }