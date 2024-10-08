import requests
import math
from utils.email_sender import email_sender, check_last_email


class ServerMonitor:
    def __init__(self, server_ip, server_eps32):
        self.server_ip = server_ip          
        self.server_esp32 = server_eps32

    def connection_server(self,):   
        try:
            conection_esp = requests.get(self.server_esp32)  
            if conection_esp.status_code == 200:         
                try:    
                    response = requests.get(self.server_ip)
                    data = response.json()           
                    temperatura = str(data['feeds'][-1]['field1'])                
                    return temperatura

                except Exception as e:
                    print(f"Erro ao conectar ao servidor: {e}")
                    return 
            else:
                print(f'A Esp32 está desligada')   
                return  
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
    

