from django.db.models import fields
from django.utils import timezone
from django import forms
from .models import Comment, Place, Post,VisitedPlace

class PostingForm(forms.ModelForm):
    title = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'textbox'}))
    content = forms.CharField(required = True, widget=forms.Textarea(attrs={'class': 'textbox'}))
    address = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'textbox'}))
    class Meta: 
        model = Post
        fields = ("place","title","content","address","image") 

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ("town",)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
