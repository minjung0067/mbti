from django.contrib import admin

# Register your models here.
from .models import User, MBTI, School, Major, School_Major

admin.site.register(User)
admin.site.register(MBTI)
admin.site.register(School)
admin.site.register(Major)
admin.site.register(School_Major)