from django import forms
from .models import profile,projo_post
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

class ProjectPostForm(forms.ModelForm):
  '''
  class that defines how the post project form shall look like
  '''
  class Meta:
    model=projo_post
    exclude=['posted_by','posted_on']  
    
