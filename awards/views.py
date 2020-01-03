from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UpdateuserForm,UpdateprofileForm,ProjectPostForm,reviewForm
from .models import profile,projo_post,reviews
from django.shortcuts import get_object_or_404,HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
import json


def home(request):
  '''
  view function to render the landing page
  '''
  posts=projo_post.get_all_posts()
  return render(request,'index.html',{"posts":posts})

@login_required(login_url='/accounts/login/')
def logout_request(request):
  '''
  view function that logout a user
  '''
  logout(request)
  return redirect('home')

@login_required(login_url='/accounts/login/')  
def user_profile(request):
  '''
  view function that renders the profile page for a user
  '''
  title=request.user
  posts=projo_post.get_user_posts(request.user.id)
  return render(request, 'profile.html',{"title":title,"posts":posts})

@login_required(login_url='/accounts/login/')  
def other_user_profile(request,username):
  person=User.objects.get(username=username)
  title=username
  posts=projo_post.get_user_posts(person.id)
  return render(request, 'others_profile.html',{"person":person,"title":title,"posts":posts})

@login_required(login_url='/accounts/login/')  
def update_profile(request):
  '''
  view function that renders the update profile form
  '''
  title='Update_profile'
  if request.method=='POST':
    user_form=UpdateuserForm(request.POST, instance=request.user)
    profile_form=UpdateprofileForm(request.POST, request.FILES, instance=request.user.profile)

    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      return redirect('profile')
  else:
    user_form=UpdateuserForm(instance=request.user)  
    profile_form=UpdateprofileForm(instance=request.user.profile)

  context={
    'user_form':user_form,
    'profile_form':profile_form,
  }  

  return render(request, 'updateprofile.html',context,{"title":title})

@login_required(login_url='/accounts/login/')  
def post_project(request):
  '''
  view function tha renders the post project form
  '''
  title='New_Post'  
  if request.method=='POST':
    form=ProjectPostForm(request.POST,request.FILES)
    if form.is_valid():
      post=form.save(commit=False)      
      post.posted_by=request.user        
      post.save()
      return redirect('home')
  else:
    form=ProjectPostForm()

    return render(request, 'new_post.html',{"title":title,"form":form})  

@login_required(login_url='/accounts/login/')  
def update_post(request,post_id):
  '''
  view function that renders the update form for a post
  '''
  post=projo_post.get_single_post(post_id)
  instance=get_object_or_404(projo_post,id=post_id)
  if request.method=='POST':
    form=ProjectPostForm(request.POST, instance=instance)
    if form.is_valid():
      post=form.save(commit=False)
      post.posted_by=request.user
      post.save()
      return redirect('single_post',post.id)
  else:
    form=ProjectPostForm(instance=instance)

  return render(request, 'update_post.html',{"form":form,"post_id":post_id})      

@login_required(login_url='/accounts/login/')  
def single_post(request,post_id):
  '''
  view function to render a single post on a page
  '''
  post=projo_post.get_single_post(post_id)
  title=post.title
  form=reviewForm()
  projo_reviews=reviews.project_reviews(post_id)
  return render(request, 'single_post.html',{"title":title,"post":post,"form":form,"reviews":projo_reviews})

@login_required(login_url='/accounts/login/')  
def add_review(request,projo_id):
  '''
  view function that saves a review for a project to the database
  '''
  if request.method=='POST':
    review_form=reviewForm(request.POST)
    project=projo_post.get_single_post(projo_id)
    if review_form.is_valid():
      review=review_form.save(commit=False)
      review.posted_by=request.user
      review.projo_id=project
      review.save()
      data={'success': 'Successfully added you review...'}
      return JsonResponse(data)



    






  

