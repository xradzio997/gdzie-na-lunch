import os
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pymongo import MongoClient

app = FastAPI()

# Pobieramy link do bazy z tzw. zmiennych środowiskowych (żeby nie trzymać hasła w kodzie!)
MONGO_URI = os.getenv("MONGO_URI")

# Łączymy się z bazą (jeśli nie ma linku, aplikacja się nie połączy)
if MONGO_URI:
    client = MongoClient(MONGO_URI)
    db = client["gdzienalunch_db"]
    collection = db["restaurants"]
else:
    collection = None

@app.get("/", response_class=PlainTextResponse)
def get_restaurants_csv():
    if collection is None:
        return "Błąd: Brak połączenia z bazą danych (sprawdź MONGO_URI)."
    
    # Pobieramy wszystkie restauracje z bazy
    restaurants = collection.find()
    
    # Tworzymy nagłówek naszego "CSV"
    csv_output = "Nazwa,Adres,Ocena\n"
    
    # Dodajemy każdą restaurację do tekstu
    for r in restaurants:
        nazwa = r.get("nazwa", "Brak nazwy")
        adres = r.get("adres", "Brak adresu")
        ocena = str(r.get("ocena", "Brak oceny"))
        
        csv_output += f"{nazwa},{adres},{ocena}\n"
        
    return csv_output