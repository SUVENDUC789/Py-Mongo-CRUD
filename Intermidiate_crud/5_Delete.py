import pymongo as p

def main():
    client = p.MongoClient('mongodb://localhost:27017')
    db = client['suvenduPymongo']
    collection = db['testPymongo']

    # Delete one record
    rec={'name': 'Bristi Bhattacharya'}
    collection.delete_one(rec)

    # Delete many record 
    rec={'name': 'Hritik Dey'}
    e=collection.delete_many(rec)
    print("Effect document : ",e.deleted_count)
   

    alldocs=collection.find()
    for i in alldocs:
        print(i)


if __name__ == "__main__":
    main()
