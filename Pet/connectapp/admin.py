from django.contrib import admin

# Register your models here.
from connectapp.models import UserInfo,PetInfo,UserPet

class UserInfoAdmin(admin.ModelAdmin):
    '''
    show userinfo
    '''
    list_display = ['name','password']

admin.site.register(UserInfo,UserInfoAdmin)

class PetInfoAdmin(admin.ModelAdmin):
    '''
    show petinfo
    '''
    list_display = ['serial_number','p_password','temprature','gps','heart_rate']

admin.site.register(PetInfo,PetInfoAdmin)

class UserPetAdmin(admin.ModelAdmin):
    '''
    show userpetinfo
    '''
    list_display = ['username','pet']

admin.site.register(UserPet,UserPetAdmin)