from django import forms
from .models import profile,projo_post,reviews
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
    fields=['title','landing_page_pic','live_link','description']  
    
class reviewForm(forms.ModelForm):
  '''
  class that defines how the review form shall look like
  '''
  class Meta:
    model=reviews
    fields=['body']
    

