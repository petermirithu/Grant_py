from rest_framework import serializers
from .models import profile,projo_post

class profileSerializer(serializers.ModelSerializer):
  '''
  class that converts profile model to json object and vice versa
  '''
  class Meta:
    model=profile
    fields=('user','bio','profile_pic','contact','git_name')

class projectSerializer(serializers.ModelSerializer):
  '''
  class that convert projects model to json format and vice versa
  '''
  class Meta:
    model=projo_post
    fields=('title','landing_page_pic','live_link','description','posted_by','posted_on','design','usability','content','total')