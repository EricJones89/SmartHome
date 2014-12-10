from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from Server.models import SerialConnections
from Server.SerialConnectionProvider import SerialConnectionProvider
from xbee_module.models import xbee_module


def index(request):
    serial_list = SerialConnections.objects.all()
    for serial in serial_list:
        serial.start_connection();
    context = {'serial_list':list(serial_list)}
    return render(request, "server/index.html", context)

def serial_connection(request):
    connection = SerialConnectionProvider.SerialConnection(name = request.POST['serial_name'] , location_url = request.POST['serial'], type = request.POST['type'])
    connection.save()
    open = connection.start_connection()
    if open:
        return HttpResponse("There was an error while opening the created port.")
    return HttpResponse("Your connection is open for buisiness!")

def add_serial_connection(request):
    serial_list = SerialConnections.get_list_of_serial_connections()
    context = {'serial_list':serial_list}
    return render(request, "server/add_serial_connection.html", context)

def program_serial_connection(request):
    serialConnection = xbee_module.objects.get(pk=request.POST["serial"])
    if isinstance(serialConnection, xbee_module):
        return redirect(serialConnection)
    return HttpResponse("no available page for this connection")