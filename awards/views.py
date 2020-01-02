from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UpdateuserForm,UpdateprofileForm
from .models import profile

def home(request):
  '''
  view function to render the landing page
  '''
  return render(request,'index.html')

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
  return render(request, 'profile.html',{"title":title})

@login_required(login_url='/accounts/login/')  
def update_profile(request):
  '''
  view function that renders the update profile form
  '''
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

  return render(request, 'updateprofile.html',context)

  

