from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url('^$',views.home,name="home"),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'^accounts/profile/$',views.user_profile,name='profile'),    
    url(r'^update/profile/$',views.update_profile,name='updateprofile'),
    url(r'^new_post/$',views.post_project,name="new_post"),
    path(r'single_post/<int:post_id>',views.single_post,name="single_post"),
    path(r'update_post/<int:post_id>',views.update_post,name="update_post"),
    path(r'profile/<username>',views.other_user_profile,name="user_profile"),
]
