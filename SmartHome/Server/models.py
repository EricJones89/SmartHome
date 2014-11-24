from django.db import models
from serial.tools import list_ports_posix
import serial
import glob
# Create your models here.


class SerialConnections(models.Model):
    name = models.CharField(max_length=200)
    location_url = models.CharField(max_length=100)

    def __str__(self):
        return ''.join(list(list_ports_posix.comports()))

    @staticmethod
    def get_list_of_serial_connections():
        return glob.glob('/dev/tty.*')

    def start_connection(self):
        try:
            self.serialConnection = serial.serial_for_url(self.location_url, timeout=3)
        except serial.SerialException as e:
            print(e)
            self.isConnected = False
            return False
        self.isConnected = self.serialConnection.isOpen();
        return self.isConnected;