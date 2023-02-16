import os
import pymongo as p 
import pandas as pd

def insert(collection):
    # insert one data 
    roll=input('Enter roll number : ')
    name=input('Enter Name : ')
    age=input('Enter age : ')
    cgpa=input('Enter Cgpa : ')
    sem=input('Enter Semester : ')

    n=collection.count_documents({'Roll':roll})
    if n ==0:
        data = {'Roll': roll, 'Name': name,'Age': age, 'Cgpa': cgpa, 'Semester': sem}
        collection.insert_one(data)
    else:
        print('Student (Roll) already exists ....')



def find(collection):
    n=collection.count_documents({})
    if n==0:
        print('No data present ...')
    else:
        # print(n)
        allData=collection.find({},{'_id': 0})
        rolld=[]
        for i in allData:
            rolld.append(i['Roll'])

        allData=collection.find({},{'_id': 0})
        nd=[]
        for i in allData:
            nd.append(i['Name'])

        allData=collection.find({},{'_id': 0})
        ad=[]   
        for i in allData:
            ad.append(i['Age'])
        
        allData=collection.find({},{'_id': 0})
        cd=[]
        for i in allData:
            cd.append(i['Cgpa'])

        allData=collection.find({},{'_id': 0})
        sd=[]
        for i in allData:
            sd.append(i['Semester'])
        
        dataset={
            'Roll':rolld,
            'Name':nd,
            'Age':ad,
            'Cgpa':cd,
            'Semester':sd
        }

        df=pd.DataFrame(dataset)
        print(df)
        input('Press any key to continue ...')
    pass

def delete(collection):
    n=collection.count_documents({})
    if n==0:
        print('No data found so you cannot perform delete Operation ...')
    else:
        roll=input('Enter roll number : ')
        ds={'Roll':roll}
        n=collection.delete_many(ds)
        print(n.deleted_count,' Rows deleted successfully')


def update(collection):
    roll=input('Enter roll Number : ')
    keys=['Roll','Name','Age','Cgpa','Semester']
    n=collection.count_documents({'Roll':roll})
    if n==0:
        print('No data found so you cannot perform update Operation ...')
    else:
        for i , v in enumerate(keys):
            if i==0:
                continue
            else:
                print("Press ",i," To update  ",v)

    # n=collection.count_documents({'Roll':roll})
    if n!=0:          
        choice = int(input('Enter number : '))
        try:
            ke=keys[choice]
            newdata=input(f'Enter {ke} : ')
            prev={'Roll':roll}
            nextt={'$set':{ke:newdata}}
            n=collection.update_many(prev,nextt)
            print('Effect row : ',n.modified_count)

        except:
            print('Enter correct index...')

    

if __name__=='__main__':

    try :
        client = p.MongoClient("mongodb+srv://suvenduc789:suvenduc789@cluster0.5hfi8pd.mongodb.net/?retryWrites=true&w=majority")
        db = client['MMCC']
        collection = db['Students']

        while True:
                keys=['Insert','Update','Delete','Show Data','Exit']
                for i , v in enumerate(keys):
                    print("Press ",i," To perform  ",v)

                choice = eval(input('Enter Your choice : '))

                if choice == 0 :
                    os.system('cls')
                    insert(collection)
                elif choice==1:
                    os.system('cls')
                    update(collection)
                elif choice==2:
                    os.system('cls')
                    delete(collection)
                elif choice==3:
                    os.system('cls')
                    find(collection)
                elif choice==4:
                    os.system('cls')
                    print('Thank you for using my program ...')
                    break
                else:
                    os.system('cls')
                    print('Enter 0 to 4 only ...')
    except:
        print('Pls connect to internet ...')
        
   