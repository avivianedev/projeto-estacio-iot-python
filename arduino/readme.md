# Monitor de Temperatura IoT com ESP8266 e DHT11
Este projeto tem como objetivo desenvolver uma aplicação de IoT que utiliza de uma placa ESP8266 NodeMCU V3 e um sensor DHT11 para monitorar a temperatura de um ambiente. O dispositivo foi configurada para enviar os dados para o ThingSpeak.
Um led é acesso a cada requisição. O prototótipo é totalmente independente, não precisa estar conectado ao computador. Ele é alimentado por uma fonte de alimentação ajustável. 

## Tecnologias Utilizadas
- IDE do Arduino: Utilizada para escrever, compilar e fazer o upload do código para a placa ESP8266. 
- ESP8266 NodeMCU: Um microcontrolador com suporte a Wi-Fi embutido, utilizado para conectar-se à rede sem fio e hospedar o servidor web.
- DHT11 Sensor de Temperatura: Sensor utilizado para medir a temperatura do ambiente. Ele comunica-se com o ESP8266 através de um dos pinos GPIO.

## Bibliotecas Utilizadas:
- ESP8266WiFi.h: Biblioteca que permite que o ESP8266 conecte-se a redes Wi-Fi e realize operações como cliente ou servidor.
- ESP8266WebServer.h: Biblioteca usada para criar um servidor web simples no ESP8266, capaz de responder a requisições HTTP.
- ESP8266mDNS.h: Biblioteca para usar o mDNS, permitindo que você acesse o ESP8266 pela rede local através de um nome amigável (ex.: esp8266.local), sem precisar conhecer o IP exato.
- DHTesp.h: Biblioteca para ler dados do sensor de temperatura DHT11. Ela facilita a obtenção da temperatura e umidade.
- ThingSpeak.h: Biblioteca utilizada para enviar os dados de temperatura do ESP8266 para a plataforma ThingSpeak, permitindo monitoramento remoto via nuvem.

## Protocolos e Serviços:
- HTTP (Hypertext Transfer Protocol): Utilizado para a comunicação entre o servidor web hospedado no ESP8266 e os clientes (navegadores) que acessam a página da temperatura. 

## Ferramentas de Controle de Versão:
- GitHub: Plataforma usada para hospedar e compartilhar o código do projeto.

## Funcionalidades
- Conexão Wi-Fi: O ESP8266 conecta-se a uma rede Wi-Fi local.
- Sensor de Temperatura: O sensor DHT11 lê a temperatura atual.
- Interface Web: A temperatura é exibida em uma página web servida pelo ESP8266. 
- Indicador LED: O LED integrado pisca ao processar solicitações de clientes.

## Componentes
- ESP8266 NodeMCU V3
- Sensor de Temperatura DHT11
- Cabos Jumpers
- Protoboard
- Fonte de Alimentação de 5V

+  Custo total: R$158.00 ( com frete incluso )

## Diagrama de Ligação
- Pino de Dados do DHT11 para D3 (GPIO 0)
- VCC do DHT11 para 3.3V
- GND do DHT11 para GND
- Pino do LED para GPIO 1 (LED integrado)

## Como Funciona
- O ESP8266 conecta-se a uma rede Wi-Fi utilizando o SSID e a senha fornecidos.
- O sensor DHT11 coleta os dados de temperatura do ambiente e envia essas informações para a plataforma ThingSpeak.
- O ThingSpeak armazena os dados na nuvem, permitindo acesso a essas informações remotamente via requisições à API.
- O LED integrado pisca quando os dados de temperatura são obtidos ou uma solicitação de cliente é processada.
- Se uma rota inexistente for acessada, uma mensagem "404 Not Found" é retornada.