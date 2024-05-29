# Użyj oficjalnego obrazu Pythona jako bazy
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj wszystkie pliki projektu do obrazu
COPY . /app

# Zainstaluj wymagane pakiety
RUN pip install --no-cache-dir -r requirements.txt

# Uruchom aplikację
CMD ["python", "app/app.py"]
