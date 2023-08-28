from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
        
class CustomUserChangForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class UserReqistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждения пароля", widget=forms.PasswordInput)
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароль не совпадают!")
        
        return cd["password2"]
    
    class Meta:
        model = User
        fields = ("username", "first_name", "email")
        
    