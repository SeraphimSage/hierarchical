from django import forms
from mptt.forms import TreeNodeChoiceField
from hierarchical_app.models import MyUser

class MyUserForm(forms.Form):

    class Meta:
        model = MyUser
        fields = ["username", "display_name"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=80)

class FolderForm(forms.Form):
    parent = TreeNodeChoiceField
    
    class Meta:
        fields = ['name', 'parent']