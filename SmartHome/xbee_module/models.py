from django.db import models
from Server.models import SerialConnections
import glob

# Create your models here.
class xbee_module(SerialConnections):
    destinationAddress = models.TextField(max_length=16);
    networkAddress = models.TextField(max_length=4);
    serialNumber = models.TextField(max_length=16);
    pan_id = models.TextField(max_length=16);
