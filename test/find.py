import pymongo as p

def dirName(pa):
    for i in dir(pa):
        print(i)

def findData():
    # connect mongodb database
    client = p.MongoClient('mongodb://localhost:27017')
    db = client['MMCC']
    collection = db['Students']
    # dirName(collection)
    # print(collection)
    alldata = collection.find({'Roll':'S-411'}, {'_id': 0})
    # alldata = collection.find().limit(3)
    # print(alldata.count())
    print(collection.count_documents({'Roll':'S-411'}))
    
    for i in alldata:
        print(i,type(i))
    


if __name__ == '__main__':
    findData()
    # dirName()
