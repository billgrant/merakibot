from meraki import meraki   
import os

# API key and ORG id exported for dev purposes
apikey = os.environ.get('APIKEY')
orgid = os.environ.get('ORGID')

class Client():
    """Class to retrieve client data from the Meraki API"""

    def __init__(self, client_id):
        """intialize client attributes."""
        self.client_id = client_id
        
    def getclient(self):
        """Gets the devices in a meraki organization """
        devices = meraki.get_device_statuses(apikey, orgid)
        
        """Finds the device(s) the client is connected to and creats a list
        with the user data and switch name"""
        for device in devices:
            client_devices = meraki.getclients(apikey, device['serial'])
            for client_device in client_devices:
                if client_device['ip'] == self.client_id:
                    client_details = Client.buildclientdetails(self, client_device, device) 
                elif client_device['mac'] == self.client_id:
                    client_details = Client.buildclientdetails(self, client_device, device)
        return client_details

    def clientinfo(self):
        """Formats the text for output to Slack"""
        message= ""
        clients = Client.getclient(self)
        for client in clients:
            for key, value in client.items():
                message += "\n" + str(key).upper() + " : " + str(value)
            return message
                
    def getnetworkname(self, networkId):
        """Gets the details about the networkId that
        was passed. Then returns them the calling function"""
        network = meraki.getnetworkdetail(apikey, networkId)
        return network['name']

    def buildclientdetails(self, client_device, device):
        client_details = []
        client_device['Connected to'] = device['name']
        client_device['network'] = Client.getnetworkname(self, device['networkId'])
        client_details.append(client_device)
        return client_details

