from math import nan
from flask import Flask, render_template
import os
from utils.server_monitor import ServerMonitor
from utils.email_sender import check_and_delete_lines

app = Flask(__name__)
SERVER_IP = os.getenv('SERVER_IP')
FILEPATH = 'email_status.txt'
c = ServerMonitor(SERVER_IP)

@app.route("/")
def index():    
    image = "erro.png" 
    condition = "Indisponível"
    message = "Erro ao obter a temperatura. Verifique sua conexão com a internet e se o sensor está ligado."
    temperature= 00.00 
    
    with open('email_status.txt', 'r') as file:
        data = file.read().splitlines()
    if c.connection_server() is not None:    
        temperature = c.fetch_temperature()   
        image, condition, message = c.evaluate_temperature()   
        check_and_delete_lines(FILEPATH)   
        return render_template("index.html", temperature=temperature, image=image,condition=condition, message=message, data=data)     
          
    return render_template("index.html", temperature=temperature, image=image,condition=condition, message=message, data=data)  


if __name__ == '__main__':    
    app.run(debug=False, host='0.0.0.0')
