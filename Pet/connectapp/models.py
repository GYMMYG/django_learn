from django.db import models

# Create your models here.
class UserInfo(models.Model):
    '''
    class UserInfo:

    period one:
    name:string(1-10) (primary key)
    password:string(6-10)

    period two:
    briefinformation:
    phone:
    wechat:
    qq:
    email:
    '''
    name = models.CharField(max_length=10,primary_key=True)
    password = models.CharField(max_length=20)


class PetInfo(models.Model):
    '''
    class  petinfo:
    serial_number(primary key):
    p_password:
    temprature:
    gps:
    heart_rate:
    '''
    serial_number = models.CharField(max_length=20,primary_key=True)
    p_password = models.CharField(max_length=20)
    temprature = models.IntegerField()
    gps = models.CharField(max_length=20)
    heart_rate = models.CharField(max_length=20)

class UserPet(models.Model):
    '''
    class userpet:react the relation between users and pets
    username:
    pet:
    '''
    username = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    pet = models.ForeignKey('PetInfo',on_delete=models.CASCADE)