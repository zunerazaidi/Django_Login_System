from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from pages.models import MyUser

class CustomUserCreationForm(UserCreationForm):
    # password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    date_of_birth = forms.DateField(label="DOB", help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = MyUser
        widgets = {'role' : forms.RadioSelect()}
        fields = ("first_name", "last_name", "email", "date_of_birth", "telephone", "role")