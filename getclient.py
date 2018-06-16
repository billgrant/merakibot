from meraki import meraki   
import os

    
def getclient(ip):
    apikey = os.environ.get('APIKEY')
    serial = os.environ.get('SERIAL') 
    """this will eventually loop through all serials"""
    clients = meraki.getclients(apikey, serial)
    
    for client in clients:
        if client['ip'] == ip:
            return client




