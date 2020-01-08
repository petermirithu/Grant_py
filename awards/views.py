from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UpdateuserForm,UpdateprofileForm,ProjectPostForm,reviewForm
from .models import profile,projo_post,reviews,preference
from django.shortcuts import get_object_or_404,HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import profileSerializer,projectSerializer


def home(request):
  '''
  view function to render the landing page
  '''
  date=dt.date.today()
  posts=projo_post.get_all_posts()
  winner=projo_post.winner_project()
  raters=preference.get_rater_users(winner.id)
  desi=winner.design
  usabi=winner.usability
  conte=winner.content
  total=winner.total

  perce_desi=(desi/100)*total
  perce_usabi=(usabi/100)*total
  perce_conte=(conte/100)*total

  context={
    'posts':posts,
    'winner':winner,
    'date':date,
    'rate_desi':perce_desi,
    'rate_usabi':perce_usabi,
    'rate_conte':perce_conte,
    'raters':raters
  }
  return render(request,'index.html',context)

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
  for post in posts:
    post.design=(post.design/100)*post.total
    post.usability=(post.usability/100)*post.total
    post.content=(post.content/100)*post.total
    
  return render(request, 'profile.html',{"title":title,"posts":posts})

@login_required(login_url='/accounts/login/')  
def other_user_profile(request,username):
  person=User.objects.get(username=username)
  title=username
  posts=projo_post.get_user_posts(person.id)
  for post in posts:
    post.design=(post.design/100)*post.total
    post.usability=(post.usability/100)*post.total
    post.content=(post.content/100)*post.total
    
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
  if request.method=='POST':
    form=ProjectPostForm(request.POST,request.FILES)
    if form.is_valid():
      post=form.save(commit=False)      
      post.posted_by=request.user        
      post.save()
      return redirect('home')
  else:
    title='New_Post'  
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
  raters=preference.get_rater_users(post.id)
  title=post.title
  form=reviewForm()
  projo_reviews=reviews.project_reviews(post_id)

  desi=post.design
  usabi=post.usability
  conte=post.content
  total=post.total

  rate_desi=(desi/100)*total
  rate_usabi=(usabi/100)*total
  rate_conte=(conte/100)*total
  return render(request, 'single_post.html',{"title":title,"post":post,"form":form,"reviews":projo_reviews,'rate_desi':rate_desi,'rate_usabi':rate_usabi,'rate_conte':rate_conte,'raters':raters})

@login_required(login_url='/accounts/login/')  
def add_review(request):
  '''
  view function that saves a review for a project to the database
  '''
  if request.method=='POST':
    review_form=reviewForm(request.POST)
    post_id_x=request.POST.get('post_id')
    post_id=int(post_id_x)    
    project=projo_post.get_single_post(post_id)
    if review_form.is_valid():
      review=review_form.save(commit=False)
      review.posted_by=request.user
      review.projo_id=project
      review.save()
      review_posted=reviews.get_review_latest()
      data={
        'success':'Successfully added your review...',
        'body':review_posted.body,
        'posted_by':review_posted.posted_by.username,
        'posted_on':review_posted.posted_on
        }
      return JsonResponse(data)

@login_required(login_url='/accounts/login/')  
def rate(request):
  '''
  view function that helps in rating a post
  '''
  if request.method == "POST":      
    design = request.POST.get("design", None)
    usability = request.POST.get("usability", None)
    content = request.POST.get("content", None) 
    post_id=request.POST.get('postID')   
    project=get_object_or_404(projo_post,id=int(post_id))
        
    try:                  
      obj_post=preference.objects.get(user=request.user,post=project)                         
      if obj_post.user == request.user:      
        data={'success': 'You have already Rated this post!'}
        return JsonResponse(data)        

    except preference.DoesNotExist:      
      rated=request.POST.get('rated_true')      
      rater=preference()
      rater.user=request.user
      rater.post=project
      rater.design=int(rated)
      rater.usability=int(rated)
      rater.content=int(rated)
      
      project.design +=int(design)
      project.usability +=int(usability)
      project.content +=int(content)
      rate_sum=int(design)+int(usability)+int(content)
      project.total+=rate_sum

      rater.save()
      project.save() 
      data={'success': 'You have successfully Rated this post! Rates update on Page reload..'}
      return JsonResponse(data)
  
@login_required(login_url='/accounts/login/')  
def search(request):
  '''
  view function that searches for projects  
  '''
  if 'search_term' in request.GET and request.GET['search_term']:
    term=request.GET.get('search_term')
    try:      
      projects=projo_post.search_project(term)      
      message=f'{term}'
      title=term
      return render(request,'search.html',{"message":message,"title":title,"projects":projects})

    except projo_post.DoesNotExist:
      message=f'{term}'
      return render(request,'search.html',{"message":message,"title":title})        

@login_required(login_url='/accounts/login/')  
def delete_project(request, post_id):
  '''
  view function that helps in deleting a project
  '''
  post=projo_post.get_single_post(post_id)
  post.delete()
  return redirect('home')


class profileList(APIView):
  def get(self, request, format=None):
    '''
    function that gets all profiles in json format
    '''
    all_profiles=profile.objects.all()
    serializers=profileSerializer(all_profiles, many=True)
    return Response(serializers.data)

class projectList(APIView):
  def get(self, request, format=None):
    '''
    function that gets all projects posted
    '''
    all_projects=projo_post.objects.all()
    serializers=projectSerializer(all_projects, many=True)
    return Response(serializers.data)


  








