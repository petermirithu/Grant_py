from django.contrib import admin
from .models import profile,projo_post,reviews,preference

# Register your models here.
admin.site.register(profile)
admin.site.register(projo_post)
admin.site.register(preference)
admin.site.register(reviews)

