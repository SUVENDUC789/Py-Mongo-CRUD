import pymongo as p 

client = p.MongoClient('mongodb://localhost:27017')
db=client['victim']
collection = db['vic_det']

f=open('log.txt','w')
f.write(f'0')
while True:
    try:
        f=open('log.txt')
        data=int(f.read())
        n=collection.count_documents({})
        if data!=n:
            f=open('log.txt','w')
            f.write(f'{n}') 
            df=collection.find({},{'com':-1})  
            df=list(df)

            print(data,n,df[len(df)-1]['com'])
    except:
        print('')
    