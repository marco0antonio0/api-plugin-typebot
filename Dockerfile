# Use a imagem selenium/standalone-chrome como base
FROM selenium/standalone-chrome

# Atualize os pacotes e instale o Python 3.10 e o pip
USER root
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-distutils && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3.10 get-pip.py && \
    rm get-pip.py

# Copie o arquivo requirements.txt e instale as dependências do Python
COPY requirements.txt /app/
RUN pip3.10 install --no-cache-dir -r /app/requirements.txt

# Copie o código fonte do aplicativo
COPY . /app/

# Defina o diretório de trabalho como /app
WORKDIR /app

# Execute o aplicativo main.py ao iniciar o contêiner
CMD ["python3.10", "main.py"]