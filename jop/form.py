from django import forms

from .models import Applyer , Jop


class Applyform (forms.ModelForm):
    class Meta :
        model = Applyer
        fields = ['name','email' , 'website' , 'cv' ,'coverletter']


class JopForm (forms.ModelForm):
    class Meta :
        model = Jop 
        fields = '__all__'
        exclude = ('slug','owner')