from django import forms


'''
-> Username
-> Email
-> Password
'''
class Registerform(forms.Form):
    username  = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
