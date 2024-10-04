import requests
import math
from utils.email_sender import email_sender, check_last_email
from datetime import datetime
import time

FILEPATH = "email_status.txt"

class ServerMonitor:
    def __init__(self, server_ip):
        self.server_ip = server_ip
           

    def connection_server(self,):           
        try:
            response = requests.get(self.server_ip)
            if response.status_code == 200:
                return response.text.strip()
            else:
                raise ConnectionError("Erro ao conectar ao servidor", response.status_code)
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")
            return      
        
    def fetch_temperature(self):        
        data = self.connection_server()
        if data:
            temperature = data.split(':')[1].strip()
            return float(temperature)
        else:
            return         
    
    def evaluate_temperature(self,):        
        temperature = self.fetch_temperature()
        if not math.isnan(temperature):
            if temperature > 26:
                image = "temperatura-alta.png"
                condition = "Temperatura quente"
                message = "Recomenda-se resfriar o ambiente." 
                if check_last_email(FILEPATH):               
                    email_sender(temperature)
                
            elif temperature < 23:
                image = "frio.png"
                condition = "Temperatura fria"
                message = "Recomenda-se aquecer o ambiente"
            else:
                image = "normal.png"
                condition = "Temperatura adequada"
                message = "Ambiente confortável"
                #A Agência de Vigilância Sanitária, a Anvisa, diz que a temperatura ideal em ambientes fechados é algo entre 23°C e 26°C
        else:
            image = "erro.png"
            condition = "Erro"
            message = "Erro ao obter a temperatura."   

        return image, condition, message
    

