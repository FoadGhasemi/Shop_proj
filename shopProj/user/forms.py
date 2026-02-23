from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # this line runs every time the form is created
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """ this loop over the dict of field objects means
        do the same styling on all the fields """
        for filed in self.fields.values():
            filed.widget.attrs.update({
                "class": "form_control"
            })

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({
                "class": "from_control"
            })

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'bio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({
                "class": "from_control"
            })

