import pymongo as p 
import os

client = p.MongoClient('mongodb://localhost:27017')
db=client['victim']
collection = db['vic_det']

# data={'com':command,'det':''}

d=os.listdir()

prev={'com':'ls'}
nextt={'$set':{'det':d}}

collection.update_one(prev,nextt)



