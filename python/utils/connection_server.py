import os
import requests


SERVER_IP = os.getenv('SERVER_IP')

def connection_server():    
    response = requests.get(f'{SERVER_IP}')
    return response       


def get_temperature():
    response = connection_server()
    temperature_data = response.text.strip()            
    temperature = float(temperature_data.split(':')[1].strip())
    return temperature