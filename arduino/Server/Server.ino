#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include "DHTesp.h"

DHTesp dht;

const char* ssid = "Vivelle_2G";
const char* password ="Lion1010";

ESP8266WebServer server(80);

const int led = 1;

void handleRoot() {  
  float temperatura = dht.getTemperature();
  
  digitalWrite(led, 1);
  Serial.print("Temperatura: ");
  Serial.print(temperatura);

  String textoHTML;
  textoHTML += "Temperatura: " + String(temperatura);
 
   
  server.send(200, "text/html", textoHTML);
  digitalWrite(led, 0);
}

void handleNotFound(){
  digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0);
}

void setup(void){
  pinMode(led, OUTPUT);
  digitalWrite(led, 0);
  Serial.begin(115200);

  dht.setup(D3, DHTesp::DHT11); // Inicializa o DHT11


  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
    
  }
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Falha na conexão Wi-Fi.");
    return; // Saia da função de setup
}
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);

  server.on("/inline", [](){
    server.send(200, "text/plain", "this works as well");
  });

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void){
  server.handleClient();
  float temperatura = dht.getTemperature();
  
  Serial.println("Temperatura: ");
  Serial.println(temperatura);
  delay(2000);
}