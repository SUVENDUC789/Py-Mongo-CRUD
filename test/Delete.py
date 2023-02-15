import pymongo as p 

def deleteData():
    client=p.MongoClient('mongodb://localhost:27017')
    db = client['MMCC']
    collection = db['Students']

    deldata={'Semester':6}
    # nextt={'$set':{'Name':'Suvendu Chowdhury'}}

    collection.delete_many(deldata)
    print('Deleted ...')
    
    pass

if __name__=='__main__':
    deleteData()