from django.shortcuts import render
from django.http import HttpResponse
from xbee_module.models import xbee_module

def index(request):
    return HttpResponse("this is not programming")

def program(request):
    context = {'serial_list':"here"}
    return HttpResponse("this is now programming")
