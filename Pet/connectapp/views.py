from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader,RequestContext
import json
from connectapp.models import PetInfo,UserInfo,UserPet


def getPetInfo(request,bid):
    pet = PetInfo.objects.get(serial_number=bid)
    data = {
    'serial_number':pet.serial_number,
    'gps': pet.gps,
    'temperature': pet.temprature,
    'heart_rate': pet.heart_rate,
    }
    return  JsonResponse(data)

def getUserInfo(request,bid):
    user = UserInfo.objects.get(name=bid)
    data = {
        'name': user.name,
    }
    return JsonResponse(data)