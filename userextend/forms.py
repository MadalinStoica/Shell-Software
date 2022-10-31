from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput


class UserExtendForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email']

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your '
                                                                                             'password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your '
                                                                                             'password confirmation'})


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your '
                                                                                             'username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your '
                                                                                             'password'})
