# l=os.listdir(os.getcwd())
# l=os.listdir()
# l=os.getcwd()
# os.chdir('terimaki')
# l=os.getcwd()
# l=os.listdir()
# print(l,type(l))


import os 

def list_of_all_class_and_Method():
    c=1
    for i in dir(os):
        if not i.startswith('_'):
            print(c,i)
            c+=1

while True:
    command=input(f'(Suvendu @ EXTRIMIS) : '+os.getcwd()+' [$] ')

    # FORWORD CHANGED DIRECTORY 
    if 'cd' in command and 'cd ..' not in command:
        folder=command.split()
        os.chdir(folder[1])
    
    # BACKWORD CHANGE DIRECTORY
    # C:\Users\suven\Desktop\Py-Mongo-CRUD\Extrimis\Live Propagration\lsd >
    elif 'cd ..' in command:
        sen = os.getcwd()
        lsen=sen.split('\\')
        d=lsen.pop()
        bpath='\\'.join(lsen)
        os.chdir(bpath)

    # AS LIKE DIR/B 
    elif 'ls' in command:
        dirslashb=os.listdir(os.getcwd())
        for i in dirslashb:
            print(i)

        