import requests as req

from pymongo import MongoClient

resp=req.get('https://soccer.sportmonks.com/api/v2.0/teams/')
product_data=resp.json()

products = product_data['products']

groceries = []

for product in products:
    if product['category'] == 'groceries':
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