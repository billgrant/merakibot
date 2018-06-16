from meraki import meraki   
import os


def getclient(ip):
    """Function that gets the client data and returns it as 
    a string"""
    apikey = os.environ.get('APIKEY')
    serial = os.environ.get('SERIAL') 
    clients = meraki.getclients(apikey, serial)
    """this will eventually loop through all serials"""
    message = ""
    for client in clients:
        if client['ip'] == ip:
           for key, value in client.items():
                message += "\n" + str(key).upper() + " : " + str(value)
           return message

