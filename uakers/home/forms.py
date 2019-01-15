from django                         import forms
from django.contrib.auth.forms      import UserCreationForm
from django.contrib.auth.models     import User
from .models                        import UserProfile, Confessions, ConfessionComment
from .choices                       import *


class SignUpForm(UserCreationForm):
    profile_year        = forms.ChoiceField(choices = YCHOICES, label="Grad year", initial='', widget=forms.Select(), required=False)
    profile_sex         = forms.ChoiceField(choices = SCHOICES, label="Sex", initial='', widget=forms.Select(), required=False)
    profile_image       = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Online link of a photo', 'autocomplete': 'off', 'onfocus': 'this.placeholder=""', 'onblur': 'this.placeholder="Online link of a photo"'}))
    profile_song        = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter the youtube link of your favorite song', 'autocomplete': 'off', 'onfocus': 'this.placeholder=""', 'onblur': 'this.placeholder="Enter the youtube link of your favorite song"'}))


    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2', 'profile_year', 'profile_sex', 'profile_image', 'profile_song')

class ConfessionsForm(forms.ModelForm):
    confession_title        = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Some confession title?', 'autocomplete': 'off', 'onfocus': 'this.placeholder=""', 'onblur': 'this.placeholder="Some confession title?"'}))
    confession_body         = forms.CharField(max_length=10000, required=True, widget=forms.Textarea(attrs={'placeholder': 'What confession do you have in mind?', 'onfocus': 'this.placeholder=""', 'onblur': 'this.placeholder="What confession do you have in mind?"'}))

    class Meta:
        model = Confessions
        fields = ('confession_title', 'confession_body')


class ConfessionCommentForm(forms.ModelForm):
    comment_body = forms.CharField(max_length=10000, required=True, widget=forms.Textarea(attrs={'placeholder': 'what do you think of the confession?', 'onfocus': 'this.placeholder=""', 'onblur': 'this.placeholder="what do you think of the confession?"'}))

    class Meta:
        model = ConfessionComment
        fields = ('comment_body',)
