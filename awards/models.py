from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.http import Http404

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
    return self.user.username

  def save_profile(self):
    '''
    function that saves user's data to profile table
    '''
    self.save()


class projo_post(models.Model):
  '''
  class that defines how projects are going to be stored
  '''
  title=models.CharField(max_length=100)
  landing_page_pic=ImageField(manual_crop='')
  live_link=models.CharField(max_length=1000)
  description=models.TextField(max_length=2000)  
  posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
  posted_on=models.DateField(auto_now_add=True)
  design=models.IntegerField(default=0)
  usability=models.IntegerField(default=0)
  content=models.IntegerField(default=0)
  total=models.IntegerField(default=0)
  

  class Meta:
    ordering=['posted_on']
    get_latest_by = 'total'

  def __str__(self):
      return self.title

  def save_post(self):
    '''
    function saves projects posted
    '''
    self.save()

  def delete_post(self):
    '''
    function that deletes a project
    '''
    self.delete()

  @classmethod        
  def get_all_posts(cls):
    '''
    function that gets all posts from the database
    '''
    posts=cls.objects.order_by('-id')
    return posts

  @classmethod
  def get_single_post(cls,post_id):
    '''
    function that gets a single post
    '''
    post=cls.objects.get(pk=post_id)
    return post

  @classmethod
  def get_user_posts(cls, user_id):
    '''
    function that gets a user's posts
    '''
    posts=cls.objects.filter(posted_by__id__contains=user_id).order_by('-id')
    return posts

  @classmethod
  def winner_project(cls):
    post=cls.objects.latest()
    return post

  @classmethod
  def search_roject(cls,post_name):
    posts=cls.objects.filter(title__icontains=post_name)
    return posts

class preference(models.Model):
  '''
  class that defines how users are going to rate a project
  '''
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  post=models.ForeignKey(projo_post, on_delete=models.CASCADE)
  design=models.IntegerField()
  usability=models.IntegerField()
  content=models.IntegerField()

  def __str__(self):
    return self.post    

  @classmethod
  def get_rater_users(cls,post_id):
    '''
    function that gets users who have rated a post
    '''
    raters=cls.objects.filter(post__id__contains=post_id)
    return raters
  
class reviews(models.Model):
  '''
  class that defines how comments achitecture shall look like
  '''
  body=models.CharField(max_length=1000)
  projo_id=models.ForeignKey(projo_post, on_delete=models.CASCADE)
  posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
  posted_on=models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.body

  @classmethod
  def project_reviews(cls,projo_id):
    '''
    function that gets all reviews related to a project
    '''
    reviews=cls.objects.filter(projo_id__id__contains=projo_id)
    return reviews


  




