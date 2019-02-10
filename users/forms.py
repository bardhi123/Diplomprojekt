from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Firstname')
    last_name = forms.CharField(max_length=30, label='Lastname')
    is_staff = forms.BooleanField(label='Are you a golf club?', required=False)
    image = forms.ImageField(required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = self.cleaned_data['is_staff']
        #user.image = self.cleaned_data['image']
        user.save()