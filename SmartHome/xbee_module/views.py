from django.shortcuts import render
from django.http import HttpResponse
from xbee_module.models import xbee_module

def index(request):
    return HttpResponse("this is not programming")

def program(request, xbee_module_id):
    xbee_module_instance = xbee_module.objects.get(pk=xbee_module_id)

    if  'serial_command' in request.POST:
        serial_command = request.POST['serial_command']


    context = {'serial_output' : "none",
               'xbee_module':xbee_module_instance}
    return render(request, "xbee_module/programModule.html", context)
