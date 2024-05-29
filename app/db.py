from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017/')  # Uwzględnij używanie Docker
db = client['nazwa_bazy_danych']

def save_data(data):
    collection = db['nazwa_kolekcji']
    collection.insert_one(data)
