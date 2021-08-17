from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(help_text="school ID", primary_key=True, default=1)
    school =  models.ForeignKey('School', on_delete = models.CASCADE,null= False, default=0)  
    mbti = models.ForeignKey('MBTI', on_delete = models.CASCADE)
    name =  models.CharField(max_length=20)
    grade =  models.CharField(max_length=4, default="21학번")
    def __str__(self):
        return self.name

class MBTI(models.Model):
    mbti =  models.CharField(max_length=4)

    def __str__(self):
        return self.mbti

class School(models.Model):
    school_id = models.BigAutoField(help_text="school ID", primary_key=True)
    school = models.CharField(max_length=20)

    def __str__(self):
        return self.school


# class Major(models.Model):
#     major = models.CharField(max_length=20)

#     def __str__(self):
#         return self.major
