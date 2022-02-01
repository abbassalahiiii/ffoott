from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        
    class meta():
        model=User
        fields=['username','email','first_name', 'last_name']

