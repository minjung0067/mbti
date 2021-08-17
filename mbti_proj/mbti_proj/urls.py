"""mbti_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mbtiapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mbtiapp.views.index, name='index'),
    path('main/', mbtiapp.views.main, name='main'),
    path('select_school/', mbtiapp.views.select_school, name='select_school'),
    path('my_school_main/', mbtiapp.views.my_school_main, name='my_school_main'),
    path('sign_up/<int:school_id>', mbtiapp.views.sign_up, name='sign_up'),
    path('result/', mbtiapp.views.result, name='result'),
    path('about_mbti/', mbtiapp.views.about_mbti, name='about_mbti'),
    path('sign_mbti/', mbtiapp.views.sign_mbti, name='sign_mbti'),
    path('create_user/', mbtiapp.views.create_user, name='create_user'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
