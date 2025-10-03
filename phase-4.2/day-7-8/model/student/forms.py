from django import forms
from student.models import Profile

# class Registration(forms.Form):
#     name = forms.CharField(error_messages={'required': 'Please enter your name'})
#     email = forms.EmailField(error_messages={'required': 'Please enter your email'})
#     password = forms.CharField(error_messages={'required': 'Please enter your password'}, widget=forms.PasswordInput)

class Registration(forms.ModelForm):
    name = forms.CharField(max_length=50)
    confirm_password = forms.CharField()
    class Meta:
        model = Profile
        fields = ['name', 'email', 'password']
        labels = {'name': 'Enter Name', 'email': 'Enter Email', 'password': 'Enter password'}
        error_messages = {
            'email' : {'required':'Please enter your email'},
            'password' : {'required':'Please enter your password'}
        }
        widgets = {
            'password' : forms.PasswordInput(attrs={'class' : 'pwsclass', 'placeholder' : 'Enter your password...'}),                'name' : forms.TextInput(attrs={'class' : 'name', 'placeholder' : 'Enter your name...'}),
            'email' : forms.TextInput(attrs={'class' : 'email', 'placeholder' : 'Enter your email...'})
        }