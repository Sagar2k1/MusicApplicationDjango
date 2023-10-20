from typing import Any
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

class RegisterForm(forms.Form):
    password = forms.CharField(label='Password',\
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',\
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({
                    'class': 'form form-control'
                })
        self.fields['first_name'].label = 'HỌ'
        self.fields['last_name'].label = 'TÊN'
        self.fields['email'].label = 'EMAIL'  
    

    
        
