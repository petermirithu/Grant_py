from django import forms
from .models import profile
from django.contrib.auth.models import User

class UpdateprofileForm(forms.ModelForm):
  '''
  class that defines how the update form for a profile shall look like
  '''
  class Meta:
    model=profile
    exclude=['user']

class UpdateuserForm(forms.ModelForm):
  '''
  class that defines how the update user form shall look like
  '''
  class Meta:
    model=User
    fields=['username','email','first_name','last_name']