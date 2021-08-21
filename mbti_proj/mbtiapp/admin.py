from django.contrib import admin

# Register your models here.
from .models import Service_User, MBTI, School 

admin.site.register(Service_User)
admin.site.register(MBTI)
admin.site.register(School)