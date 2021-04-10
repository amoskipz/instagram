from django import forms
from .models import Profile,Image,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['likes','profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['picture', 'comment_title']


class MessageForm(forms.Form):
    subject = forms.CharField(max_length=100)
    To = forms.CharField(max_length=100)

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user         