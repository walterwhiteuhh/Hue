import requests

user = 'g6KZIhPm71RZBmwM7QvEZIWvDeX9QR9pjsvPa8v'
ip = '192.168.0.15'

class Hue:
    def __init__(self, user, ip, lamp):
        self.user = user 
        self.ip = ip 
        self.lamp = lamp
        self.url = 'http://{}/api/{}/lights/{}/state/'.format(self.ip, self.user, self.lamp)
    
    def set_lamp(self, is_on):
        data = {'on' : is_on}
        requests.put(self.url, json=data)
    
    def set_color(self, color):
        if color == "ORANGE":
            data = {"on": True, "sat": 254, "bri": 254, "hue": 10880}    
        #elif            :
        #    data = {}
        #elif            :
        #    data = {}
        requests.put(self.url, json=data)
        
if __name__ == "__main__":
    pass

            
    