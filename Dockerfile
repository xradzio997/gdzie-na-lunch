# 1. Używamy oficjalnego, lekkiego obrazu Pythona
FROM python:3.11-slim

# 2. Tworzymy folder /app wewnątrz naszego kontenera
WORKDIR /app

# 3. Kopiujemy listę bibliotek i instalujemy je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopiujemy całą resztę naszego kodu do kontenera
COPY . .

# 5. Komenda, która uruchomi nasz serwer po starcie kontenera
# Używamy portu 8080, bo taki domyślnie lubi Google Cloud
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]