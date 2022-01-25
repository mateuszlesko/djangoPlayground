from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewMemberForm(UserCreationForm):
    email = forms.EmailField(required = True,widget=forms.TextInput(attrs={'class': 'textbox'}))
    username = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'textbox'}))
    password1 = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'textbox'}))
    password2 = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'textbox'}))
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def confirm(self,commit=False):
        user = super(NewMemberForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user