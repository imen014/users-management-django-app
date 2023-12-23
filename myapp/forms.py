from django import forms


class MyFirstForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    email = forms.EmailField()