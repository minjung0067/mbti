from django.db import models

# Create your models here.
class Service_User(models.Model):
    user_id = models.BigAutoField(help_text="school ID", primary_key=True)
    school =  models.ForeignKey('School', on_delete = models.CASCADE, null= False, default=1)  
    mbti = models.ForeignKey('MBTI', on_delete = models.CASCADE, default=1, null=False)
    name =  models.CharField(max_length=20)
    grade =  models.CharField(max_length=4, default="21학번")
    def __str__(self):
        return self.name

class MBTI(models.Model):
    mbti_id = models.BigAutoField(help_text="mbti ID", primary_key=True,default = 1, null=False)
    mbti =  models.CharField(max_length=10)

    def __str__(self):
        return self.mbti

class School(models.Model):
    school_id = models.BigAutoField(help_text="school ID", primary_key=True)
    school = models.CharField(max_length=20)


    def __str__(self):
        return self.school

