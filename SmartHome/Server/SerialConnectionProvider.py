from Server.models import SerialConnections
from xbee_module.models import xbee_module

class SerialConnectionProvider:

    @staticmethod
    def SerialConnection(type = "default", location_url = "", name = "some name" ):
        if type == "xBee":
            return xbee_module(name = name, location_url = location_url)
        else :
            return SerialConnections(name=name, location_url=location_url)