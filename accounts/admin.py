# Finally we have to update our accounts/admin.py.
# The admin is a common place to manipulate user data there is tight coupling between the built-in user and the admin
# We'll extend the existing UserAdmin into CustomUseradmin and tell django to use our new forms and custom user model
# We can also list any user attributes we want but for now will just focus on three: e-mail, username, superuser status

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Here we have again that circular import to enforces the idea of making one single reference to the customusermodel
CustomUser = get_user_model()


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
