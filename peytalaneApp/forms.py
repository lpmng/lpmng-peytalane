from django import forms

class InscriptionExtForm(forms.Form):
    lastName = forms.CharField(label="Nom",max_length=100)
    firstName = forms.CharField(label="Prénom",max_length=100)
    mail = forms.EmailField(label="Mail")
    username = forms.CharField(label="Pseudo",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,label="Mot de passe")
    passwordConfirm = forms.CharField(widget=forms.PasswordInput,label="Confirmation mot de passe")

class InscriptionEistiForm(forms.Form):
    username = forms.CharField(label="Pseudo",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,label="Mot de passe")

class LoginForm(forms.Form):
    username = forms.CharField(label="Pseudo",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,label="Mot de passe")