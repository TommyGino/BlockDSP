FROM python:3.8-slim

WORKDIR /app

# Copia tutti i file del blocco nel container
COPY . /app

# Installa le dipendenze richieste
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta standard usata da Edge Impulse
EXPOSE 4446

# Comando di avvio: esegui il file dsp.py come server
ENTRYPOINT ["python", "dsp.py"]
