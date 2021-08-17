from django.contrib import admin

# Register your models here.
from .models import User, MBTI, School 

admin.site.register(User)
admin.site.register(MBTI)
admin.site.register(School)