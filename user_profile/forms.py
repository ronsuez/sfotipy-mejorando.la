from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserCreationEmailForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        """

        :param self:
        :param args:
        :param kwargs:
        """
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(self, *args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        #django function , returns None/User.
        self.user_cache = authenticate(email=email, password=password)

        #The user doesn't exists
        if self.user_cache is None:
            raise forms.ValidationError('Incorrect or unexisting User')
        #The user exists but is not active yet.
        elif not self.user_cache.is_active:
            raise forms.ValidationError('Inactive User')

        #all good
        return self.cleaned_data

    #returns the user stored in user_cache
    def get_user(self):
        return self.get_user()
