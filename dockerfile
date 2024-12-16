# Usar a imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo de dependências e instalar
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY src/ /app/src

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "src/app/app.py"]
