from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomAccount


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=30, help_text='Required')
    email = forms.EmailField(label='Enter Email', max_length=200, help_text='Required',
                             error_messages={'required': 'Sorry, you will need an email'})
    first_name = forms.CharField(label='Enter Your first name', min_length=1)
    last_name = forms.CharField(label='Enter Your last name', min_length=1)
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomAccount
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')

    def clean_password2(self):
        cleaned_data = self.cleaned_data

        if cleaned_data.get("password") != cleaned_data.get("password2"):
            raise forms.ValidationError("Passwords should match!")
        return cleaned_data.get("password2")


class ChangeAccountDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomAccount
        fields = (
            'first_name', 'last_name', 'country',
            'phone_number', 'postcode', 'town_city',
            'address', 'post_office_name',
            'post_office_code', 'about')
