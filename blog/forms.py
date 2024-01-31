from django import forms
from .models import Blog,ContactModel

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_Login_Form(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name', 'last_name', 'email', 'password1',]
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description','author']
        
        widgets = {
               'description': forms.Textarea(attrs={'rows': 20, 'cols': 50}),
        }
        
        
        
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email','your_message']
        
        widgets = {
               'your_message': forms.Textarea(attrs={'rows': 20, 'cols': 50}),
        }
        