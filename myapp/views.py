from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib import sessions,messages
from django.contrib.auth import logout
import random
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.sites.shortcuts import get_current_site
import uuid
# hirer mail confirm
# selected   mail
# update profile for both
# Create your views here.   


def index(request):
    data=None
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            firstName=request.POST['first_name']
            lastName=request.POST['last_name']
            City=request.POST['city']
            se_user=request.POST['email']
            se_user=se_user.strip()
            State=request.POST['state']
            Mobile=request.POST['mobile']
            Password=request.POST['password']
            Skill=request.POST['skill']
            Experience=request.POST['experince']
            Age=request.POST['age']
            Zip=request.POST['zip']
            Gender=request.POST['gender']
            token=str(uuid.uuid4())
            try:
                data=signUpModel.objects.get(email=se_user)
            except Exception as e:
                print(e)    
            if data:
                messages.error(request, "Account Alreday exists Please Login")
            else:
                signUpModel.objects.create(first_name=firstName,
                                            last_name=lastName,
                                            email=se_user,
                                            city=City,
                                            state=State,
                                            mobile=Mobile,
                                            password=Password,
                                            skill=Skill,
                                            experince=Experience,
                                            age=Age,
                                            zip=Zip,
                                            gender=Gender,
                                            VerificationToken=token                                       
                                        )
                site=get_current_site(request)
                id_data=signUpModel.objects.get(email=se_user)
                request.session['id']=id_data.id
                try: 
                    subject='Verify Your Account'
                    message=f'Verify your WeHire account by clicking following link http://{site}/verify-account/{token}'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[se_user]
                    send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)
                    print("Email Sent")
                    return redirect('verify')
                except Exception as e:
                    messages.success(request, "Please Enter Valid email")
                    print(e)
            # se_mail=send_email_token(token=token,email=se_user,site=site)
            # if se_mail=='something went wrong':
            #     messages.success(request, "Please Enter Valid email")
            #     print(se_mail)
            # else:    
            #     print(se_mail)
            #     
        elif request.POST.get('login')=='login':
            usrnm=request.POST['email']
            usrpass=request.POST['password']
            login=signUpModel.objects.filter(email=usrnm,password=usrpass)
            if login:
                data=signUpModel.objects.get(email=usrnm)
                request.session['user']=usrnm
                request.session['id']=data.id
            else:
               messages.warning(request, "Enter Valid Username Or Password.")
               return redirect('/')

    cat=catagory_list.objects.all()
    cudata=request.session.get('id')
    job=jobModel.objects.all().order_by('-timestamp')   
    if cudata:
            cudata=signUpModel.objects.get(id=cudata)
    if cudata is None:
        cudata=('none')
    return render(request,'index.html',{'cudata':cudata,'cat':cat,'job':job})

def about(request):
    cudata=None
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            firstName=request.POST['first_name']
            lastName=request.POST['last_name']
            City=request.POST['city']
            se_user=request.POST['email']
            se_user=se_user.strip()
            State=request.POST['state']
            Mobile=request.POST['mobile']
            Password=request.POST['password']
            Skill=request.POST['skill']
            Experience=request.POST['experince']
            Age=request.POST['age']
            Zip=request.POST['zip']
            Gender=request.POST['gender']
            token=str(uuid.uuid4())
            try:
                data=signUpModel.objects.get(email=se_user)
            except Exception as e:
                print(e)    
            if data:
                messages.error(request, "Account Alreday exists Please Login")
            else:
                signUpModel.objects.create(first_name=firstName,
                                            last_name=lastName,
                                            email=se_user,
                                            city=City,
                                            state=State,
                                            mobile=Mobile,
                                            password=Password,
                                            skill=Skill,
                                            experince=Experience,
                                            age=Age,
                                            zip=Zip,
                                            gender=Gender,
                                            VerificationToken=token                                       
                                        )
                site=get_current_site(request)
                id_data=signUpModel.objects.get(email=se_user)
                request.session['id']=id_data.id
                try: 
                    subject='Verify Your Account'
                    message=f'Verify your WeHire account by clicking following link http://{site}/verify-account/{token}'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[se_user]
                    send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)
                    print("Email Sent")
                    return redirect('verify')
                except Exception as e:
                    messages.success(request, "Please Enter Valid email")
                    print(e)
        elif request.POST.get('login')=='login':
            usrnm=request.POST['email']
            usrpass=request.POST['password']
            login=signUpModel.objects.filter(email=usrnm,password=usrpass)
            if login:
                data=signUpModel.objects.get(email=usrnm)
                request.session['user']=usrnm
                request.session['id']=data.id
            else:
                messages.add_message(request, messages.INFO, "Invalid username or password")
    cudata=request.session.get('id')    
    if cudata:
            cudata=signUpModel.objects.get(id=cudata)
    if cudata is None:
        cudata=('none')      
    return render(request,'about.html',{'cudata':cudata,'catagory':catagory})
        
def catagory(request,id):
    cat=catagory_list.objects.all()
    cat_list=jobModel.objects.filter(catagory_id=id).order_by('-timestamp')
    cudata=request.session.get('id')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            firstName=request.POST['first_name']
            lastName=request.POST['last_name']
            City=request.POST['city']
            se_user=request.POST['email']
            se_user=se_user.strip()
            State=request.POST['state']
            Mobile=request.POST['mobile']
            Password=request.POST['password']
            Skill=request.POST['skill']
            Experience=request.POST['experince']
            Age=request.POST['age']
            Zip=request.POST['zip']
            Gender=request.POST['gender']
            token=str(uuid.uuid4())
            try:
                data=signUpModel.objects.get(email=se_user)
            except Exception as e:
                print(e)    
            if data:
                messages.error(request, "Account Alreday exists Please Login")
            else:
                signUpModel.objects.create(first_name=firstName,
                                            last_name=lastName,
                                            email=se_user,
                                            city=City,
                                            state=State,
                                            mobile=Mobile,
                                            password=Password,
                                            skill=Skill,
                                            experince=Experience,
                                            age=Age,
                                            zip=Zip,
                                            gender=Gender,
                                            VerificationToken=token                                       
                                        )
                site=get_current_site(request)
                id_data=signUpModel.objects.get(email=se_user)
                request.session['id']=id_data.id
                try: 
                    subject='Verify Your Account'
                    message=f'Verify your WeHire account by clicking following link http://{site}/verify-account/{token}'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[se_user]
                    send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)
                    print("Email Sent")
                    return redirect('verify')
                except Exception as e:
                    messages.success(request, "Please Enter Valid email")
                    print(e)
        elif request.POST.get('login')=='login':
            usrnm=request.POST['email']
            usrpass=request.POST['password']
            login=signUpModel.objects.filter(email=usrnm,password=usrpass)
            if login:
                data=signUpModel.objects.get(email=usrnm)
                request.session['user']=usrnm
                request.session['id']=data.id
        elif request.POST.get('job')=='job':
            apply_valid=applyForm(request.POST,request.FILES)
            if apply_valid.is_valid():
                apply_valid.save()  
                print('applied') 
            else:
                print(apply_valid.errors)       
    if cudata:
            cudata=signUpModel.objects.get(id=cudata)
    if cudata is None:
        cudata=('none') 
    return render(request,'catagory.html',{'cat_list':cat_list,'cat':cat,'cudata':cudata})
    
def apply(request,id):
    job_data=jobModel.objects.get(id=id)
    cudata=request.session.get('id')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            firstName=request.POST['first_name']
            lastName=request.POST['last_name']
            City=request.POST['city']
            se_user=request.POST['email']
            se_user=se_user.strip()
            State=request.POST['state']
            Mobile=request.POST['mobile']
            Password=request.POST['password']
            Skill=request.POST['skill']
            Experience=request.POST['experince']
            Age=request.POST['age']
            Zip=request.POST['zip']
            Gender=request.POST['gender']
            token=str(uuid.uuid4())
            try:
                data=signUpModel.objects.get(email=se_user)
            except Exception as e:
                print(e)    
            if data:
                messages.error(request, "Account Alreday exists Please Login")
            else:
                signUpModel.objects.create(first_name=firstName,
                                            last_name=lastName,
                                            email=se_user,
                                            city=City,
                                            state=State,
                                            mobile=Mobile,
                                            password=Password,
                                            skill=Skill,
                                            experince=Experience,
                                            age=Age,
                                            zip=Zip,
                                            gender=Gender,
                                            VerificationToken=token                                       
                                        )
                site=get_current_site(request)
                id_data=signUpModel.objects.get(email=se_user)
                request.session['id']=id_data.id
                try: 
                    subject='Verify Your Account'
                    message=f'Verify your WeHire account by clicking following link http://{site}/verify-account/{token}'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[se_user]
                    send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)
                    print("Email Sent")
                    return redirect('verify')
                except Exception as e:
                    messages.success(request, "Please Enter Valid email")
                    print(e)
        elif request.POST.get('login')=='login':
            usrnm=request.POST['email']
            usrpass=request.POST['password']
            login=signUpModel.objects.filter(email=usrnm,password=usrpass)
            if login:
                data=signUpModel.objects.get(email=usrnm)
                request.session['user']=usrnm
                request.session['id']=data.id

        elif request.POST.get('apply')=='apply':
            udata=signUpModel.objects.get(id=cudata)
            usr=udata.email
            job_id=request.POST['id_of_job']
            valid=applyModel.objects.filter(email=usr,id_of_job=job_id)
            if valid:
                #checking pending
                messages.info(request, "You have already applied..")   
            else:
                apply=applyForm(request.POST,request.FILES)
                if apply.is_valid():
                    apply.save()
                    return redirect('/')
                else:
                    print(apply.errors)
 
    if cudata:
            cudata=signUpModel.objects.get(id=cudata)
    if cudata is None:
        cudata=('none')             
    return render(request,'applyjob.html',{'cudata':cudata,'job_data':job_data})

def hireerindex(request):
    cat=catagory_list.objects.all()
    hi_email=request.session.get('hi_email')
    data=hireerModel.objects.get(email=hi_email)
    if request.method=='POST':
        if request.POST.get('addjob')=='addjob':
            addjob=jobForm(request.POST,request.FILES)    
            if addjob.is_valid():
                addjob.save()
                print("Job added")
            else:
                print(addjob.errors)
    jobdata=jobModel.objects.filter(added_by=data.business_name).order_by('-timestamp')                
    return render(request,'hireerindex.html',{'data':data,'cat':cat,'jobdata':jobdata})


def hireerlogin(request):
    gen_otp='none'
    se_data=request.session.get('hi_email')
    hirerdata=None    
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            email=request.POST['email']
            try:
                hirerdata=hireerModel.objects.get(email=email)
                messages.warning(request,'Account already exists please login')
            except hireerModel.DoesNotExist:
                pass
            if hirerdata == None:
                try:
                    subject='Verify Your Account'
                    gen_otp=random.randint(100000,199999)
                    message=f'Your one time password for wehire account is {gen_otp}'
                    email_from=settings.EMAIL_HOST_USER
                    recipient_list=[email]
                    send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)
                    print("Email Sent")
                    user=hireerForm(request.POST)
                    if user.is_valid():
                        user.save(commit=False)
                except Exception as e:
                    print(e)
        if request.POST.get('otp')==('otp'):
            otp=request.POST['otp']
            if otp == gen_otp:
                user.save()
            
            # if signup.is_valid():
            #     signup.save()
            #     usrnm=request.POST.get('email')
            #     data=hireerModel.objects.get(email=usrnm)
            #     request.session['hi_id']=data.id
            #     request.session['hi_email']=usrnm
            #     se_data=request.session.get('user')
            #     return redirect('hireerindex')
            # else:
            #     print(signup.error)
        elif request.POST.get('login')=='login':
            usr_email=request.POST['email']
            usr_pass=request.POST['password']
            login=hireerModel.objects.filter(email=usr_email,password=usr_pass)
            if login:
                data=hireerModel.objects.get(email=usr_email)
                request.session['hi_email']=usr_email
                request.session['hi_id']=data.id
                se_data=request.session.get('hi_email')
    if se_data is None:
        se_data='none'
    else:
        se_data=se_data
    print(se_data)                     
    return render(request,'hireerlogin.html',{'se_data':se_data,'gen_otp':gen_otp})

def manageReq(request):
    se_data=request.session.get('hi_email')
    data=hireerModel.objects.get(email=se_data)
    jobdata=jobModel.objects.filter(added_by=data.business_name).order_by('-timestamp')
    #add form for delete button and toggle modal for edit job data
    return render(request,'managereq.html',{'data':data,'jobdata':jobdata})

def managerRequest(request,business_name):
    se_data=request.session.get('hi_email')
    data=hireerModel.objects.get(email=se_data)
    request_data=applyModel.objects.filter(applyto=business_name).order_by('-timestamp')
    if request_data:
        pass
    else:
        request_data='none'     
    return render(request,'managerequests.html',{'request_data':request_data,'data':data})

def hired(request):
    if request.method=='POST':
        company=request.POST['company']
        date=request.POST['date']
        time=request.POST['time']
        street=request.POST['street']
        city_with_pin=request.POST['city']
        mobile=request.POST['number']
        email_id=request.POST['email']
        user_id=request.POST['id']
        applier_data=applyModel.objects.get(id=user_id)
        company=request.POST['company']
        fname=applier_data.first_name 
        lname=applier_data.last_name
        age=applier_data.age
        gender=applier_data.gender
        newuser=hiredModel.objects.create(first_name=fname,last_name=lname,email=email_id,mobile=mobile,age=age,gender=gender,hired_by=company)  
    Name=f"{applier_data.first_name}" + f"{applier_data.last_name}"
    email_message=f""" hii {Name}, \n\t\t you requested in {company} and they Looked at Your resume that you send to them via our website and they are interested in it because of that they scheduled \n your interview at {date} {time} at their office.\n\n\n \t\tAddress:\n\t\t\t\n\t\t\t\t{street}\n\t\t\t\t{city_with_pin}\n\nFor More contact +91 {mobile}\n\n\t\t\t\t\t\tThank You"""
    email_subject='Interview Notice'
    email_from=settings.EMAIL_HOST_USER
    to_email=[email_id]
    send_mail(subject=email_subject,message=email_message,from_email=email_from,recipient_list=to_email)
    parameters=applier_data.applyto
    return HttpResponseRedirect(reverse('hirednotice', args=(parameters,)))

def userlogout(request):
    if request.POST:
        if request.POST.get('hire_se')=='hire_se':
            logout(request)
            return redirect('hireerlogin')
        elif request.POST.get('user_se')=='user_se':
            logout(request)
        return redirect('/')


def VerifyUserMessage(request):
    cudata=None
    try:
        uid=request.session.get('id')
        cudata=signUpModel.objects.get(id=uid)
    except Exception as e:
        print(e)
    if cudata:
        pass
    else:
        cudata='none'       
    return render(request,'verify.html',{'cudata':cudata})


def verifyUser(request,token):
    try:
        user_id=request.session.get('id')
        user_data=signUpModel.objects.filter(id=user_id,VerificationToken=token)
        if user_data.is_valid():
            user_data.is_varified=True
            user_data.save()
            print("verified")
            return render(request,'verification.html')
    except Exception as e:
            print(e)
    

def forgetPassword(request):
    message=None
    if request.method=='POST':
        email=request.POST['reset_email'].strip()
        try:
            udata=signUpModel.objects.get(email=email)
            Resettoken=str(uuid.uuid4())
            udata.PassresetToken=Resettoken
            udata.save()
            subject='Reset your wehire Password'
            site=get_current_site(request)
            message=f'Reset your account password by  by clicking following link http://{site}/reset-password/{Resettoken}'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[email]
            send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)
            message='sent'

        except Exception as e:
            print(e)
            print('invalid')
            message='error'
            print(email)
                
    return render(request,'forgetPass.html',{'message':message})

def ResetPassword(request,token):
    message='none'
    try:
        udata=signUpModel.objects.get(PassresetToken=token)
    except signUpModel.DoesNotExist:
        message='expired'
    if request.method=='POST':
        NewPassword=request.POST['password']
        udata.password=NewPassword
        udata.PassresetToken=None
        udata.save()
        return redirect('/')
    return render(request,'resetpass.html',{'message':message})

def feedback(request):
    if request.method=='POST':
        review=FeedbackForm(request.POST)
        if review.is_valid():
            review.save()
            print("review save")
        else:
            print(review.errors)    
    return render(request,'feedback.html')

def forgetPasshirer(request):
    alert_message= 'none'
    if request.method=='POST':
        email=request.POST['reset_email']
        site=get_current_site(request)
        try:
            udata=hireerModel.objects.get(email=email)
            resetToken=str(uuid.uuid4())
            udata.passresetToken=resetToken
            udata.save()
            subject='Password reset'
            message=f'To reset your password click following link http://{site}/reset-pass-hirer/{resetToken}'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[email]
            send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)
            alert_message='Email Sent'
        except  hireerModel.DoesNotExist:
            alert_message='Enter valid email'    
        except Exception as e:
            print(e)
    return render(request,'forgethirer.html',{'alert_message':alert_message})            

def HirerResetPass(request,token):
    message='none'
    try:
        udata=hireerModel.objects.get(passresetToken=token)
    except hireerModel.DoesNotExist:
        message='expired'        

    if request.method=='POST':
            udata.password=request.POST['password']
            udata.passresetToken=None
            udata.save()
            message='success'
    return render(request,'hirerpassreset.html',{'message':message})

def linkExpired(request):
    return HttpResponse('Link Expired')
