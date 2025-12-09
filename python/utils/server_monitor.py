import os
import requests
import math

from utils.email_sender import email_sender, check_last_email

SERVER_EPS32 = os.getenv('SERVER_EPS32')
MAX_SAFE_TEMP = 26.0
MIN_SAFE_TEMP = 23.0

class ServerMonitor:
    def __init__(self, server_url):
        self.server_url = server_url      
        
    def connection_server(self,):   
        try:                 
            response = requests.get(self.server_url, timeout=5)
            data = response.json()  
            temperature = str(data['feeds'][-1]['field1'])     
            print(f"Conectado ao servidor. Temperatura recebida: {temperature}°C")           
            return temperature             
                             
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")
            return 
    

    def fetch_temperature(self):        
        data = self.connection_server()
        
        if data is not None:            
            try:
                return float(data)
            except ValueError:
                return math.nan
        else:
            return math.nan    
    
    def evaluate_temperature(self,):              
        temperature = self.fetch_temperature()

        if not math.isnan(temperature):
            
            if temperature > MAX_SAFE_TEMP:
                image = "temperatura-alta.png"
                condition = "Temperatura quente"
                message = "Recomenda-se resfriar o ambiente." 
                if check_last_email():               
                    email_sender(temperature)
                
            elif temperature < MIN_SAFE_TEMP:
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

        return image, condition, message, temperature
    

