from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader,RequestContext
import json


def getPetInfo(request):
    return HttpResponse('gy')

def getUserInfo(request):
    return HttpResponse('gy')