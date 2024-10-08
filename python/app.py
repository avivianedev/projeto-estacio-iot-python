from math import nan
from flask import Flask, render_template
import os
from utils.server_monitor import ServerMonitor
from utils.email_sender import check_and_delete_lines
from dotenv import load_dotenv
from utils.email_sender import status_mail

load_dotenv()
app = Flask(__name__)

API_URL = os.getenv('API_URL')
SERVER_EPS32 = os.getenv('SERVER_EPS32')
FILEPATH = 'email_status.txt'
c = ServerMonitor(API_URL, SERVER_EPS32)

@app.route("/")
def index():    
    image = "erro.png" 
    condition = "Indisponível"
    message = "Erro ao obter a temperatura. Verifique sua conexão com a internet e se o sensor está ligado."
    temperature= 00.00     
   
    if c.connection_server() is not None:    
        temperature = c.fetch_temperature()   
        image, condition, message = c.evaluate_temperature()   
        check_and_delete_lines()   
        return render_template("index.html", temperature=temperature, image=image,condition=condition, message=message, data=status_mail)     
          
    return render_template("index.html", temperature=temperature, image=image,condition=condition, message=message, data=status_mail)  


if __name__ == '__main__':    
    app.run(debug=False, host='0.0.0.0')