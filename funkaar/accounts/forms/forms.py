from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import FunkaarUser

'''
Created on Feb 15, 2016

@author: grs065
'''
class FunkaarUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(FunkaarUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = FunkaarUser
        fields = ("email",)

class FunkaarUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(FunkaarUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = FunkaarUser
        fields = '__all__'