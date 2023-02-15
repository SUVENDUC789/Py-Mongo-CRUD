import pymongo as p

def main():
    client = p.MongoClient('mongodb://localhost:27017')

    db = client['suvenduPymongo']
    print("List of all collection are : ",db.list_collection_names())
    # collection = db['testPymongo']

    # list all database 
    allDataBase=client.list_database_names()
    print(allDataBase)

    # print all database related details 
    d=client.list_databases()
    for i in d :
        print(i)


if __name__=='__main__':
    main()