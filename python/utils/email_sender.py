import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import datetime
import time

load_dotenv()

EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

email_interval = 20 * 60  # 20 minutos em segundos
current_time = time.time()
PATHFILE = "email_status.txt"

def email_sender(temperature):  
    #Construção do e-mail
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER 
    msg['Subject'] = 'Alerta de Temperatura Quente' 
    body = f"""
    <p>A temperatura atual está muito alta: {temperature}°C.</p
    <p>Recomenda-se resfriar o ambiente imediatamente.</p>
    <p>Localização: Sala: xxx, Andar x</p
    <p>Atenção! Um novo e-mail será enviado em <strong>20 minutos</strong> caso a situação não seja normalizada.</p
    
    <p>Abs, A Gerencia</p>
    """
    msg.attach(MIMEText(body, 'html'))   
      
    try:
        #Conectando ao servidor SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER,EMAIL_PASSWORD)

        #Enviando o e-mail
        server.sendmail(EMAIL_SENDER, msg['To'], msg.as_string())   
        # Salvando o horario atual no arquivo     
        save_email_status(PATHFILE, current_time) 
                 
        print(f"Email de alerta enviado com sucesso! Enviado em {current_time}")
    except Exception as e:
        print(f"Erro ao enviar o email: {e}")
    finally:
        server.quit() #Encerrando a conexão. 

def load_email_status(PATHFILE):
    try:
        with open(PATHFILE, 'r') as f:
            return f.read()
    except FileNotFoundError:
            return {"last_email_time": 0}
    
def check_and_delete_lines(PATHFILE):    
    try:
        with open(PATHFILE , 'r') as file:
            lines = file.readlines()
            if len(lines) > 20:
                with open(PATHFILE, 'w') as file:
                    file.truncate(0)  # Limpa o conteúdo do arquivo
                    print(f"O arquivo tinha mais de 20 linhas e foi esvaziado.")
            else:
                print(f"O arquivo tem {len(lines)} linhas, nada foi alterado.")
    except Exception as e:
        print(f'Erro ao ler o arquivo', e)


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