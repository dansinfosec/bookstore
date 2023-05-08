# Here we import get_user_model which points to 'AUTH_USER_MODEL = 'accounts.CustomUser' in our settings.py
# This line of code points to our CustomUser() in our accounts/models.py
# This enforces the idea of making one single reference to the customusermodel
from django.contrib.auth import get_user_model

# Here we import 'UserCreationForm' and 'UserChangeForm' which will both be extended
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Here we create two new forms that extand the base user forms imported above this line


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # Specifiying our CustomUserModel
        model = get_user_model()
        # display e-mail and username; password is implicitly included by default
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
