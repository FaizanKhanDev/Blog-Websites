from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post, Contact
from django.core import validators


class SignForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
       model = User
       fields = ['username','first_name','last_name','email']
       labels = {
        'first_name' : 'First Name',
        'last_name':'Last Name',
        'email': 'Email'
       }
       widgets = {
            'username' :forms.TextInput(attrs={'placeholder':'username','class':'form-control'}),
            'first_name' :forms.TextInput(attrs={'class':'form-control'}),
            'last_name' :forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.EmailInput(attrs={'class':'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofucus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))



class Postform(forms.ModelForm):
    class Meta:
        model =  Post
        fields = ['title','desc']
        labels = {
            'title':'Title',
            'desc':'description'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'desc' :forms.Textarea(attrs={'class':'form-control'})
        }




class Contact_Form(forms.ModelForm):
    class Meta:
        model =  Contact
        fields = ['full_name','phone_number','email','comment']
        labels = {
            'full_name':'Full Name',
            'phone_number':'Phone Number',
            'email':'Your Email',
            'comment':'Leave a comment'
        }
        widgets = {
            'full_name' : forms.TextInput(attrs={'placeholder':'Enter Your Full Name','class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'Enter a Valid Email','class':'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder':'Tell Us More Do not shy','class':'form-control'}),
         } 
        error_messages = {
                'full_name' : {'required':'Full  name is Required'},
                'email' :{'required':'email is required'},
                'comment' :{'required':'Please Write Somethings'}
        }



class EditAdminProfile(UserCreationForm):
    password: None
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'})),
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']