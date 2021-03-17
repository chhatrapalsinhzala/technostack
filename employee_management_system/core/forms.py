from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput)
    password = forms.CharField(label=("Password"),widget=forms.PasswordInput)


