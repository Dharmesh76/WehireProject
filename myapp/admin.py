from django.contrib import admin
from .models import *
# Register your models here.
class admin_cat(admin.ModelAdmin):
    list_display=['name']

class admin_hired(admin.ModelAdmin):
    list_display=['first_name','last_name','email','mobile','age','gender','hired_by']

class admin_feedback(admin.ModelAdmin):
    list_display=['FirstName','LastName','email','phone','message']

admin.site.register(catagory_list,admin_cat)
admin.site.register(hiredModel,admin_hired)
admin.site.register(feedbackModel,admin_feedback)