# IoT Monitor de Temperatura
Este projeto é um sistema de monitoramento de temperatura utiliznado a placa ESP8266 NodeMCU V3 e sensor DHT11. 
A aplicação coleta a temperatura de um ambiente e a exibe em uma página web, utilizando um servidor web integrado na ESP8266. 
O frontend, construído em Flask, faz requisições ao endereço da ESP8266 para exibir as informações na interface de modo automático. 
O sistema inclui um disparo de e-mail autompatico para o time de manutenção para notificar sobre a necessidade de acerto na temperatura.
A página na web conta com uma renderização condicional conforme o valor da temperatura obtido no sensor e o histórico com a datas onde foi necessário realizar ajuste na temperatura.

## Funcionalidades
- Monitoramento de temperatura em tempo real: O sistema coleta dados de temperatura usando o sensor DHT11 e os exibe em uma página web.
- Serviço de backend com Flask: O frontend em Flask faz uma requisição HTTP ao servidor ESP8266 e exibe as informações da temperatura.
- Disparo de e-mail de alerta: Um e-mail é enviado automaticamente para ajuste da temperatura caso o valor esteja acima do limite considerado ideal pela ANVISA   para ambientes fechados. Foi implemtado uma rotina de cobrança ( reenvio de e-mail ) caso a situação não esteja normalizada em até 20 minutos.
- Renderização condicional de temperatura: Dependendo do valor obtido (frio, adequado ou quente), a interface altera a exibição da imagem e mensagem associada.
- Sistema independente: O protótipo funciona com uma fonte de alimentação externa, sem necessidade de estar conectado a um computador.

## Tecnologias Utilizadas
### Hardware:
- ESP8266 NodeMCU V3
- Sensor de temperatura DHT11
- LED indicador
- Fonte de alimentação ajustável

### Software:
-VS Code - IDE para Programação do código.
-Flask (backend e renderização do frontend)
-Python (lógica de backend e requisições HTTP)
-Arduino IDE (para programar a ESP8266)
-HTML/CSS (para exibição dos dados)

## Bibliotecas Utilizadas
### O projeto depende das seguintes bibliotecas Python:
- Flask==3.0.3: Framework web utilizado para a construção do frontend.
- Python-Dotenv==1.0.1: Carrega variáveis de ambiente de um arquivo .env.
- Pywin32==306: Biblioteca para integração com o Windows.
- Requests==2.32.3: Biblioteca HTTP usada para fazer requisições ao servidor da ESP8266.

### O projeto depende das seguintes bibliotecas Esp8266:
- ESP8266WiFi.h: Biblioteca que permite que o ESP8266 conecte-se a redes Wi-Fi e realize operações como cliente ou servidor.
- ESP8266WebServer.h: Biblioteca usada para criar um servidor web simples no ESP8266, capaz de responder a requisições HTTP.
- ESP8266mDNS.h: Biblioteca para usar o mDNS, permitindo que você acesse o ESP8266 pela rede local através de um nome amigável (ex.: esp8266.local), sem precisar conhecer o IP exato.
- DHTesp.h: Biblioteca para ler dados do sensor de temperatura DHT11. Ela facilita a obtenção da temperatura e umidade.

## Estrutura do Projeto
Projeto-Estácio-IoT/
├── arduinio/
│   └── Server/               
├── evidencias/               
├── python/
│   ├── .env                 
│   ├── .venv                
│   ├── requirements.txt                 
│   ├── static/   
│   │    └──assets             
│   │       ├── temperatura-alta.png
│   │       ├── frio.png
│   │       ├── normal.png
│   │       └── erro.png
│   ├── index.css 
│   ├──reset.css 
│   ├── templates/
│   │   └── index.html     
│   ├── utils/
│   │   ├── email_sender.py   
│   │   └── server_monitor.py 
│   └── app.py                
└── .gitignore             
