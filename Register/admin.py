from django.contrib import admin
from .models import CustomUser
# Register your models here.
@admin.register(CustomUser) 
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id','Name','email'] 
    