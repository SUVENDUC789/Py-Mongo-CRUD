import pymongo as p
# mongodb+srv://suvenduc789:<password>@cluster0.5hfi8pd.mongodb.net/test

def performMongoDbWithPyMongo():
    # client = p.MongoClient('mongodb+srv://suvenduc789:suvenduc789@cluster0.5hfi8pd.mongodb.net/test')

    
    client = p.MongoClient("mongodb+srv://suvenduc789:suvenduc789@cluster0.5hfi8pd.mongodb.net/?retryWrites=true&w=majority")
    # db = client.test

    # print(client)
    db = client['MMCC']
    # print(db)
    collection = db['Students']
    # print(collection)

    # data = {'Roll': 'S-412', 'Name': 'Suvendu',
    #         'Age': 20, 'Cgpa': 7.1, 'Semester': 6}

    # collection.insert_one(data)

    dataSet=[
        {'Roll': 'S-412', 'Name': 'Suvendu','Age': 20, 'Cgpa': 7.1, 'Semester': 6},
        {'Roll': 'S-411', 'Name': 'Supratim','Age': 20, 'Cgpa': 7.2, 'Semester': 6},
        {'Roll': 'S-444', 'Name': 'Debarpan','Age': 20, 'Cgpa': 7.3, 'Semester': 6},
        {'Roll': 'S-420', 'Name': 'Hritik','Age': 20, 'Cgpa': 6.9, 'Semester': 6},
        {'Roll': 'S-410', 'Name': 'Sujan','Age': 19, 'Cgpa': 8.3, 'Semester': 6}
    ]
    collection.insert_many(dataSet)
    print('Insert Data Successfull ...')
    pass


if __name__ == '__main__':
    performMongoDbWithPyMongo()
    pass
