import os

from flask import Flask, render_template
from dotenv import load_dotenv

from utils.server_monitor import ServerMonitor
from utils.email_sender import status_mail

load_dotenv()
app = Flask(__name__)

API_URL = os.getenv('API_URL')
if not API_URL:
    raise RuntimeError("API_URL não configurada. Defina a variável de ambiente API_URL.")

server_monitor = ServerMonitor(API_URL)

DEFAULT_IMAGE = "erro.png"
DEFAULT_CONDITION = "Indisponível"
DEFAULT_MESSAGE = (
    "Erro ao obter a temperatura. Verifique sua conexão com a internet e se o sensor está ligado."
)

def build_temperature_context():
    temperature = 0.0
    image = DEFAULT_IMAGE
    condition = DEFAULT_CONDITION
    message = DEFAULT_MESSAGE

    if server_monitor.connection_server():        
        image, condition, message, temperature = server_monitor.evaluate_temperature()

    return {
        "temperature": temperature,
        "image": image,
        "condition": condition,
        "message": message,
        "data": status_mail,
    }


@app.route("/")
def index():    
    ctx = build_temperature_context()       
    return render_template("index.html", temperature=ctx["temperature"],
        image=ctx["image"],
        condition=ctx["condition"],
        message=ctx["message"],
        data=ctx["data"],)     
          


if __name__ == '__main__':    
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug, host='0.0.0.0')