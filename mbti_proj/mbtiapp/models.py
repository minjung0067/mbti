from django.db import models

# Create your models here.

class User(models.Model):
    major =  models.ForeignKey('Major', on_delete = models.CASCADE)           
    name =  models.CharField(max_length=20)
    mbti = models.ForeignKey('MBTI', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class MBTI(models.Model):
    mbti =  models.CharField(max_length=4)

    def __str__(self):
        return self.mbti

class School(models.Model):
    school = models.CharField(max_length=20)

    def __str__(self):
        return self.school

class Major(models.Model):
    school = models.ForeignKey('School', on_delete = models.CASCADE, default=1, null=True)
    major = models.CharField(max_length=100, null=True) 

    def __str__(self):
        return self.major