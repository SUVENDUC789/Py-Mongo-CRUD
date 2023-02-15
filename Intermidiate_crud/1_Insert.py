import pymongo as p


def main():
    client = p.MongoClient('mongodb://localhost:27017')
    db = client['suvenduPymongo']
    collection = db['testPymongo']

    # Insert only one dictionary
    d = {'name': 'Suvendu Chowdhury', 'age': 20,
         'Dept': 'Bsc', 'cgpa': 7.1, 'clg': 'MMCC'}
    collection.insert_one(d)

    # Insert Many dictionary
    Data = [
        {'_id': 1, 'name': 'Bristi', 'age': 20-1, 'Dept': 'Bsc',
            'cgpa': 'Semester Not clear', 'clg': 'MMCC'},
        {'_id': 2, 'name': 'Hritik', 'age': 20,
            'Dept': 'Bsc', 'cgpa': 6.9, 'clg': 'MMCC'},
        {'_id': 3, 'name': 'Debarpan', 'age': 20,
            'Dept': 'Bsc', 'cgpa': 7.2, 'clg': 'MMCC'},
        {'_id': 4, 'name': 'Supratim Majumder', 'age': 20,
            'Dept': 'Btech', 'cgpa': 'NA', 'clg': 'HETC'},
    ]

    collection.insert_many(Data)
    print('Data insert success fully')


if __name__ == "__main__":
    main()
