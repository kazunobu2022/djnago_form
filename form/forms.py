from django import forms

class TextForm(forms.Form):
    text = forms.CharField()
    box = forms.CharField()