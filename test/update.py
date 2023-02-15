import pymongo as p 

def updateData():
    client=p.MongoClient('mongodb://localhost:27017')
    db = client['MMCC']
    collection = db['Students']

    prev={'Name':'Suvendu'}
    nextt={'$set':{'Name':'Suvendu Chowdhury'}}

    n=collection.update_many(prev,nextt)
    print('Effect row : ',n.modified_count)
    
    pass

if __name__=='__main__':
    updateData()