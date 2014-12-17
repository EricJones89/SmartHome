from django.db import models
from Server.models import SerialConnections
import serial
import glob

# Create your models here.
class xbee_module(SerialConnections):
    destinationAddress = models.TextField(max_length=16);
    networkAddress = models.TextField(max_length=4);
    serialNumber = models.TextField(max_length=16);
    pan_id = models.TextField(max_length=16);

    HIGH_ADDRESS = "HIGH_ADDRESS"
    programHighAddress = "ATDH="
    printHighAddressBits = bytes("ATDH\u000D", "utf-8")

    LOW_ADDRESS = "LOW_ADDRESS"
    programLowAddress = "ATDL="
    printLowAddress = b'ATDL'


    def get_absolute_url(self):
        return "/xbee_module/program/%i/" % self.id

    def send_command(self, commands):
        if len(commands.keys()) > 0:
            self.start_connection()
            if self.isConnected:
                self.serialConnection.write(b"+++")
                response = self.serialConnection.read(3)
                print(response)
                if response == b'OK\r':

                    self.serialConnection.write(bytes(self.programHighAddress + commands[self.HIGH_ADDRESS] + '\r', 'utf-8'))
                    self.serialConnection.read(3)
                    self.serialConnection.write(bytes(self.programLowAddress + commands[self.LOW_ADDRESS] + '\r', 'utf-8'))
                    self.serialConnection.read(3)
                    self.serialConnection.write(self.printHighAddressBits);
                    newResponse = self.serialConnection.read(4)
                    print(newResponse)


