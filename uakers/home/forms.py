from django                         import forms
from django.contrib.auth.forms      import UserCreationForm
from django.contrib.auth.models     import User
from .models                        import UserProfile, Confessions
from .choices                       import *


class SignUpForm(UserCreationForm):
    profile_year        = forms.ChoiceField(choices = YCHOICES, label="Grad year", initial='', widget=forms.Select(), required=False)
    profile_sex         = forms.ChoiceField(choices = SCHOICES, label="Sex", initial='', widget=forms.Select(), required=False)
    profile_image       = forms.CharField(required=False, help_text="You can choose an image that expresses you")

    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2', 'profile_year', 'profile_sex', 'profile_image')

class ConfessionsForm(forms.ModelForm):
    confession_title        = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Confession title', 'autocomplete': 'off'}))
    confession_body         = forms.CharField(max_length=10000, required=True, widget=forms.Textarea(attrs={'placeholder': 'Write your confession'}))

    class Meta:
        model = Confessions
        fields = ('confession_title', 'confession_body')
