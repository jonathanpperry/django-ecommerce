from django.contrib import admin
from .models import UserBase

admin.site.register(UserBase)


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_lenth=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
                             'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model - UserBase
        fields = ('user_name', 'email')
