import pymongo as p 

client = p.MongoClient('mongodb://localhost:27017')
db=client['victim']
collection = db['vic_det']

command=input('Enter command : ')
data={'com':command,'det':''}
collection.insert_one(data)

df=collection.find()
for i in df:
    print(i)
