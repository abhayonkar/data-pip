import requests as req

from pymongo import MongoClient
import json

resp = req.get('https://data.nasa.gov/resource/y77d-th95.json')
product_data = resp.json()

print(product_data)

groceries = []

for product in product_data:
    if product.get('fall') == 'Fell':
        groceries.append(product)

try:
    client=MongoClient('mongodb://localhost:27017/')
    print("MongoDB Connection Successfully!")
    db=client['pymo1']
    col=db['product']
    col.insert_many(groceries)
    print("Data Inserted Successfully!")
except:
    print("Buddy Check -code one more time!")
finally:
    col=None
    db=None
    client=None