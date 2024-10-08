import requests
import math
from utils.email_sender import email_sender, check_last_email
import os

SERVER_EPS32 = os.getenv('SERVER_EPS32')

class ServerMonitor:
    def __init__(self, server_ip):
        self.server_ip = server_ip      
        
    def connection_server(self,):   
        try:                 
            response = requests.get(self.server_ip, timeout=5)
            data = response.json()           
            temperatura = str(data['feeds'][-1]['field1'])                
            return temperatura             
                             
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")
            return 
    

    def fetch_temperature(self):        
        data = self.connection_server()
        if data:            
            return float(data)
        else:
            return         
    
    def evaluate_temperature(self,):        
        temperature = self.fetch_temperature()
        if not math.isnan(temperature):
            if temperature > 26:
                image = "temperatura-alta.png"
                condition = "Temperatura quente"
                message = "Recomenda-se resfriar o ambiente." 
                if check_last_email():               
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
    

