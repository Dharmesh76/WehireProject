from django.db import models

# Create your models here.
class signUpModel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    password=models.TextField(default=None)
    skill=models.TextField(default='')
    experince=models.BigIntegerField(default='')
    age=models.TextField(default='')
    zip=models.BigIntegerField(default=1)
    gender=models.CharField(max_length=10,default='')
    VerificationToken=models.CharField(max_length=200)
    is_varified=models.BooleanField(default=False)
    PassresetToken=models.CharField(max_length=100,blank=True)
    

class hireerModel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    business_name=models.CharField(max_length=40)   
    email=models.EmailField()
    address=models.TextField()
    state=models.CharField(max_length=15)
    zip=models.BigIntegerField()
    password=models.CharField(max_length=40)
    passresetToken=models.CharField(max_length=50,blank=True)



class catagory_list(models.Model):
    name=models.CharField(max_length=30)


class jobModel(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    logo=models.ImageField(upload_to="image")
    salary=models.TextField()
    catagory=models.ForeignKey(catagory_list, on_delete=models.CASCADE)
    location=models.TextField()
    job_description=models.TextField()
    added_by=models.TextField()
    recuiredage=models.TextField(default='')
    recuiredskill=models.TextField(default='')

class applyModel(models.Model):
   
    timestamp = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    cv=models.FileField(upload_to="cv",default="")
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    zip=models.BigIntegerField()
    skill=models.TextField()
    experince=models.BigIntegerField()
    age=models.TextField()
    applyto=models.TextField()
    gender=models.CharField(max_length=10)
    applied_for=models.TextField()
    id_of_job=models.BigIntegerField()

class hiredModel(models.Model): 
    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    age=models.TextField()
    gender=models.CharField(max_length=10)
    hired_by=models.TextField()

class feedbackModel(models.Model):
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.TextField()