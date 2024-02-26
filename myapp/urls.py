from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('catagory/<int:id>/',views.catagory,name="catagory"),
    path('hireerlogin/',views.hireerlogin,name="hireerlogin"),
    path('hireerindex/',views.hireerindex,name="hireerindex"),
    path('managereq/',views.manageReq,name='managereq'),
    path('apply-job/<int:id>/',views.apply),
    path('manage-requests/<slug:business_name>',views.managerRequest,name="hirednotice"),
    path('hirednotice/',views.hired,name='hired'),
    path('verify-user/',views.VerifyUserMessage,name="verify"),
    path('verify-account/<str:token>/',views.verifyUser),
    path('forget-password/',views.forgetPassword),
    path('reset-password/<str:token>/',views.ResetPassword),
    path('user-feedback/',views.feedback),
    path('forget-pass-hirer',views.forgetPasshirer),
    path('reset-pass-hirer/<str:token>/',views.HirerResetPass),
    path('linkexpired',views.linkExpired,name='expired'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   