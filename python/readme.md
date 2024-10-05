# Frontend - IoT Cloud Monitor de Temperatura - Python
Este documento descreve o frontend da aplicação de monitoramento de temperatura baseada em IoT, utilizando Flask para a interface web que exibe a temperatura monitorada pelo sensor DHT11 conectado à placa ESP8266 NodeMCU V3. O Flask faz uma requisição à API do ThingSpeak e exibe as informações da temperatura.

## Funcionalidades
- Exibição de temperatura em tempo real: O frontend realiza requisições periódicas para exibir a temperatura atual.
- Renderização condicional de status: Dependendo do valor da temperatura, a interface exibe diferentes imagens e mensagens:
    - Temperatura adequada: Entre 23°C e 26°C, com uma imagem de "ambiente confortável".
    - Temperatura quente: Acima de 26°C, recomendando resfriar o ambiente.
    - Temperatura fria: Abaixo de 23°C, recomendando aquecer o ambiente.
- Sistema de alerta para manutenção: Se a temperatura ultrapassar os 26°C, um e-mail é enviado automaticamente para a equipe de manutenção, solicitando correção da temperatura. Caso a situação não seja resolvida em até 20 minutos, um novo e-mail será disparado, e isso continuará ocorrendo até que a temperatura volte ao nível adequado.
- Exibição das datas e horários dos últimos acionamentos na Home.

## Estrutura do Frontend

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
