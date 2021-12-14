from django.utils import timezone
from django import forms

class PostingForm(forms.Form): 
    title = forms.CharField(label='Title of the post', max_length=32)
