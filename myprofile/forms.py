from django import forms
from .models import UpdateProfile

class NewProfile(forms.ModelForm):
    class Meta:
        model = UpdateProfile
        exclude = ['editor', 'modified']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }