from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите логин", "class": "class-group"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Введите пароль", "class": "class-group"}
        )
    )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        if user and user.email:
            self.fields["email"].widget.attrs["readonly"] = True
            self.fields["email"].widget.attrs["class"] = "profile-input readonly"
        else:
            self.fields["email"].widget.attrs["placeholder"] = "Введите ваш email"

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "image", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Введите имя"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Введите фамилию"}),
            "username": forms.TextInput(
                attrs={"placeholder": "Введите имя пользователя", "readonly": True}
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Введите email"})
        }
