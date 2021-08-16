from django import forms
from mbtiapp.models import User, School, Major, Mbti


class Submitform(forms.Form):
    school = forms.ModelChoiceField(queryset=School.objects.distinct('school'),to_field_name="school")
    major = forms.ModelChoiceField(queryset=Major.objects.distinct('major'),to_field_name="major")
    name = forms.CharField(max_length=12)
    mbti = forms.ModelChoiceField(queryset=Mbti.objects.distinct('Mbti'),to_field_name="Mbti")