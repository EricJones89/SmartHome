from django.shortcuts import render
from django.http import HttpResponse
from xbee_module.models import xbee_module

def program(request):
    context = {'serial_list':"here"}
    return render(request, "xbee_module/index.html", context)
