# Usa a imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Flask irá rodar
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
