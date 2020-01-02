from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

class profile(models.Model):
  '''
  class that defines on how to store user data
  '''
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  bio=models.CharField(max_length=1000,blank=True)
  profile_pic=ImageField(blank=True,manual_crop='')
  contact=models.CharField(max_length=15,blank=True)
  git_name=models.CharField(max_length=100,blank=True)
  
  def __str__(self):
    return self.profile_pic
  

