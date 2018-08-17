from django import forms


class AddName(forms.Form):
    name = forms.CharField()