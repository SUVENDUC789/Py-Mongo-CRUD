# data={
# "_id": 'client-1',
# "input": command,
# "output": "",
# "isIssued": True
# }

import pymongo as p

client = p.MongoClient('mongodb://localhost:27017')
db = client['victim']
collection = db['vic_det']


while True:
    command = input('Enter command : ')
    if command == 'exit':
        # collection.delete_many({})
        print('exit this loop ...')
        break
    prev = {"_id": 'client-1'}
    nextt = {'$set': {"input": command, "isIssued": True}}
    n = collection.update_many(prev, nextt)

