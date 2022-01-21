from django.db.models import fields
from django.utils import timezone
from django import forms
from .models import Comment, Place, Post,VisitedPlace

class PostingForm(forms.ModelForm):
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

class LikeForm(forms.ModelForm):
    class Meta:
        model = VisitedPlace
        fields = ("likeIt",)

