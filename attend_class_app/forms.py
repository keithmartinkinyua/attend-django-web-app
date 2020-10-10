from django import forms

class Uploadphoto(forms.Form):
    image = forms.ImageField()