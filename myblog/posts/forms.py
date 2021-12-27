from django.db.models import fields
from django.utils import timezone
from django import forms
from .models import Place, Post

class PostingForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ("place","title","content","address","image") 

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ("town",)
