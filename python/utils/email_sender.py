import win32com.client as win32
import os
import pythoncom
import datetime
import time


EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
email_interval = 20 * 60  # 20 minutos em segundos
current_time = time.time()
PATHFILE = "email_status.txt"

def email_sender(temperature):        
    try:
        pythoncom.CoInitialize()
        outlook = win32.Dispatch('Outlook.application')        
        mail = outlook.CreateItem(0)       
        mail.Subject = "Alerta de Temperatura Quente"
        mail.To = EMAIL_RECEIVER      
        mail.HTMLBody = f"""
        <p>A temperatura atual está muito alta: {temperature}°C.</p
        <p>Recomenda-se resfriar o ambiente imediatamente.</p>
        <p>Localização: Sala: xxx, Andar x</p
        <span>Atenção! Um novo e-mail será enviado em <strong>20 minutos</strong> caso a situação não seja normalizada.</span
        <p>Abs, A Gerencia</p>
        """
        mail.Send()  
        save_email_status(PATHFILE, current_time)          
        print("Email de alerta enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o email: {e}")

def load_email_status(PATHFILE):
    try:
        with open(PATHFILE, 'r') as f:
            return f.read()
    except FileNotFoundError:
            return {"last_email_time": 0}


def save_email_status(PATHFILE, status):
    formatted_time = datetime.datetime.fromtimestamp(status).strftime('%d/%m/%Y %H:%M:%S')
    try:
        with open(PATHFILE, "a") as f:            
            f.write(f'{formatted_time}\n') 
    except Exception as e:
        return{"Erro ao salvar a informação", e}
    
def check_last_email(PATHFILE):
    try:
        with open(PATHFILE, "r") as f:
            lines = f.readlines()   

            if not lines:
                print("Nenhum envio anterior encontrado.")
                return True
            
            last_time_str = lines[-1].strip() 
            last_time_str = last_time_str.replace('"', '')
            last_time = datetime.datetime.strptime(last_time_str, '%d/%m/%Y %H:%M:%S')

            # Pega o horário atual
            current_time = datetime.datetime.now()

            # Calcula a diferença em minutos
            time_difference = (current_time - last_time).total_seconds() / 60

            if time_difference > 20:
                print("Já passaram mais de 20 minutos desde o último envio.")
                return True
            else:
                print( f"Ainda não se passaram 20 minutos. Tempo decorrido: {time_difference:.2f} minutos.")
                return False

    except Exception as e:   
        print(f"Erro ao verificar o horário {e}")     
        return 