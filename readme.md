# IoT Cloud Monitor de Temperatura - Python
- Este projeto é um sistema de monitoramento de temperatura utiliznado a placa ESP8266 NodeMCU V3 e sensor DHT11. 
- A aplicação coleta a temperatura de um ambiente e envia os dados para o ThingSpeak, uma plataforma de IoT baseada em nuvem. O frontend, construído em Flask e implantado no Railway, faz requisições à API do ThingSpeak para exibir as informações de temperatura em uma página web de modo automático
- O sistema inclui um disparo de e-mail autompatico para o time de manutenção para notificar sobre a necessidade de acerto na temperatura.
- A página na web conta com uma renderização condicional conforme o valor da temperatura obtido no sensor e o histórico com a datas onde foi necessário realizar ajuste na temperatura.

## Componentes
- ESP8266 NodeMCU V3
- Sensor de Temperatura DHT11
- Cabos Jumpers
- Protoboard
- Fonte de Alimentação de 5V

+  Custo total: R$158.00 ( com frete incluso )

## Funcionalidades
- Monitoramento de temperatura em tempo real: O sistema coleta dados de temperatura usando o sensor DHT11 e os exibe em uma página web.
- Envio dos dados de temperatura para o ThingSpeak.
- Serviço de backend com Flask: O frontend em Flask faz uma requisição à API do ThingSpeak e exibe as informações da temperatura.
- Disparo de e-mail de alerta: Um e-mail é enviado automaticamente para ajuste da temperatura caso o valor esteja acima do limite considerado ideal pela ANVISA   para ambientes fechados. Foi implemtado uma rotina de cobrança ( reenvio de e-mail ) caso a situação não esteja normalizada em até 20 minutos.
- Renderização condicional de temperatura: Dependendo do valor obtido (frio, adequado ou quente), a interface altera a exibição da imagem e mensagem associada.
- Sistema independente: O protótipo funciona com uma fonte de alimentação externa, sem necessidade de estar conectado a um computador.

## Tecnologias Utilizadas
- IDE do Arduino: Utilizada para escrever, compilar e fazer o upload do código para a placa ESP8266.
- ESP8266 NodeMCU: Um microcontrolador com suporte a Wi-Fi embutido, utilizado para coletar os dados do sensor de temperatura e enviar as informações para a plataforma ThingSpeak via Wi-Fi.
- DHT11 Sensor de Temperatura: Sensor utilizado para medir a temperatura do ambiente. Ele comunica-se com o ESP8266 através de um dos pinos GPIO.
- ThingSpeak: Plataforma IoT baseada em nuvem que armazena os dados de temperatura recebidos do ESP8266 e disponibiliza uma API para consulta dos dados.
- Railway: Plataforma utilizada para fazer o deploy da aplicação Flask, que acessa a API do ThingSpeak e exibe os dados de temperatura.
- Flask: Framework Python utilizado para criar o servidor backend e renderizar o frontend da aplicação, exibindo a temperatura coletada.
- Python: Utilizado no backend para fazer requisições à API do ThingSpeak, processar os dados e implementar a lógica de disparo de e-mails de alerta


## Bibliotecas Utilizadas
### O projeto depende das seguintes bibliotecas Python:
- Flask==3.0.3: Framework web utilizado para a construção do frontend.
- Python-Dotenv==1.0.1: Carrega variáveis de ambiente de um arquivo .env.
- SMTPLIB: Biblioteca para envio de e-mails.
- Requests: Biblioteca HTTP usada para fazer requisições ao ThingSpeak
- ThingSpeak - Biblioteca utilizada para enviar os dados de temperatura do ESP8266 para a plataforma ThingSpeak, permitindo monitoramento remoto via nuvem.

### O projeto depende das seguintes bibliotecas Esp8266:
- ESP8266WiFi.h: Biblioteca que permite que o ESP8266 conecte-se a redes Wi-Fi e realize operações como cliente ou servidor.
- ESP8266WebServer.h: Biblioteca usada para criar um servidor web simples no ESP8266, capaz de responder a requisições HTTP.
- ESP8266mDNS.h: Biblioteca para usar o mDNS, permitindo que você acesse o ESP8266 pela rede local através de um nome amigável (ex.: esp8266.local), sem precisar conhecer o IP exato.
- DHTesp.h: Biblioteca para ler dados do sensor de temperatura DHT11. Ela facilita a obtenção da temperatura e umidade.
- ThingSpeak.h: Biblioteca utilizada para enviar os dados de temperatura do ESP8266 para a plataforma ThingSpeak, permitindo monitoramento remoto via nuvem.

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
