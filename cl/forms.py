from cl.models import Profile, Ad
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location',)

class ItemsForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['item', 'price', 'department', 'description', 'location', 'condition', 'picture']
        exclude = ['created_at', 'updated_at']

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
