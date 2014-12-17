from django.shortcuts import render
from django.http import HttpResponse
from xbee_module.models import xbee_module

def index(request):
    return HttpResponse("this is not programming")

def program(request, xbee_module_id):
    xbee_module_instance = xbee_module.objects.get(pk=xbee_module_id)

    commands = {}
    if xbee_module.HIGH_ADDRESS in request.POST:
        commands[xbee_module.HIGH_ADDRESS] = request.POST[xbee_module.HIGH_ADDRESS]

    if xbee_module.LOW_ADDRESS in request.POST:
        commands[xbee_module.LOW_ADDRESS] = request.POST[xbee_module.LOW_ADDRESS]

    xbee_module_instance.send_command(commands)


    context = {'serial_output': "none",
               'xbee_module': xbee_module_instance}
    return render(request, "xbee_module/programModule.html", context)
