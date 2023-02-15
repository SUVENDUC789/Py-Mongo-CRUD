import pymongo as p


def dif_dive_pymongo():
    for i in dir(p):
        print(i)


def main():
    client = p.MongoClient('mongodb://localhost:27017')
    db = client['suvenduPymongo']
    collection = db['testPymongo']

    # first document data print
    one=collection.find_one()
    print(one)

    # using filter
    one=collection.find_one({'name':'Bristi'})
    print(one)

    # see all data (using filter)
    allDoc = collection.find({'Dept': 'Bsc'}, {'_id': 0, 'name': 1})
    for i in allDoc:
        print(i)

    # see all data (Without using filter)
    allDoc=collection.find()
    for i in allDoc:
        print(i)


if __name__ == "__main__":
    main()
