import pymongo as p 

client = p.MongoClient('mongodb://localhost:27017')
db=client['victim']
collection = db['vic_det']

while True:
    command=input('Enter command : ')
    collection.insert_one({'com':command})

    if command=='exit':
        collection.delete_many({})
        print('exit this loop ...')
        break
