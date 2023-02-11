from django import forms
from django.contrib.auth.forms import UserCreationForm

from pages.models import MyUser


class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(label="DOB", help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = MyUser
        widgets = {'role': forms.RadioSelect()}
        fields = ("first_name", "last_name", "email", "date_of_birth", "telephone", "role")
