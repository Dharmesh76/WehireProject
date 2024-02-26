from django import forms
from .models import *

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
]

class signupForm(forms.ModelForm):
    class Meta:
        model=signUpModel
        fields='__all__'

class hireerForm(forms.ModelForm):
    class Meta:
        model=hireerModel
        fields='__all__'  

class jobForm(forms.ModelForm):
    class Meta:
        model=jobModel
        fields='__all__'

class applyForm(forms.ModelForm):
    class Meta:
        model=applyModel
        fields='__all__'   

class updateForm(forms.ModelForm):
    class Meta:
        model=signUpModel
        fields=['first_name','last_name','email','city','state','mobile','skill','experince','age','zip','gender','is_varified'] 

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=feedbackModel
        fields='__all__'
