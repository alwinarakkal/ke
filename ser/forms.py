from django import forms
from .models import Post,Item,quantity
from django.contrib.auth.models import User


class ser_req(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    
class buy(forms.ModelForm):     
    class Meta:                
        model = Item              
        fields = '__all__'           

class number(forms.ModelForm):     #new
    class Meta:                 #new
        model = quantity               #new
        fields = '__all__'           #new
    