from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserFormRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "email", "username", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super(UserFormRegister, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
