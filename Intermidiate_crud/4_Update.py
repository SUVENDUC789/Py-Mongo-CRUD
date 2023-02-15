import pymongo as p

def main():
    client = p.MongoClient('mongodb://localhost:27017')
    db = client['suvenduPymongo']
    collection = db['testPymongo']

    prev={'name': 'Bristi bhattacharya'}

    # $set is atomic operator in mongoDb Database 
    nextt={"$set":{"name":"Bristi Bhattacharya"}}
    # collection.update_one(prev,nextt)#update method use 
    up=collection.update_many(prev,nextt)#update method use (change many document)
    print("Effect document :",up.modified_count)

    alldocs=collection.find()
    for i in alldocs:
        print(i)


if __name__ == "__main__":
    main()
