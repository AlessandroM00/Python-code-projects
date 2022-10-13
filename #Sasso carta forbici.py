#Rock, paper, scissors in italian version
#Code by: Alessandro Multari
#13/10/2022

import random
import time

def visualize_choose(n):
    if(n==1):
        return ('sasso')
    elif(n==2):
        return ('carta')
    elif(n==3):
        return ('forbici')

def compare_choose(user, pc):     #-1 vittoria pc  /   0 pareggio     /   1 vittoria user
    if(user=='s'):
        user=1
    elif(user=='c'):
        user=2
    elif(user=='f'):
        user=3

    if(user==pc):
        return 0
    elif(user==1 and pc==2):
        return -1
    elif(user==1 and pc==3):
        return 1
    elif(user==2 and pc==1):
        return 1
    elif(user==2 and pc==3):
        return -1
    elif(user==3 and pc==1):
        return -1
    elif(user==3 and pc==2):
        return 1


print("Buongiorno, benvenuto a sasso, carta e forbici... Ti va di giocare? y/n    ")
s=True
while s:
    start=input()
    start=start.lower()
    if(start!='y' and start!='n'):
        print("Perfavore, devi inserire una y=yes o una n=no\n")
    else:
        s=False

if(start=='n' or start=='N'):
    exit("Arrivederci!! :) ")

pc_score=0
user_score=0
game=True
s=True
partita=1
while (game):
    print("Partita n", partita, '\n')
    print("Sasso, carta, forbici:\n Inserisci una 's' per sasso, una 'c' per carta, una 'f' per forbici")
    s=True
    while s:
        ch_user=input()
        ch_user=ch_user.lower()
        if (ch_user!='s' and ch_user!='c' and ch_user!='f'):
            print("Perfavore, devi inserire un valore valido (s - c - f) \n")
        else:
           s=False
    
    print("Sto scegliendo")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    random.seed(a=None, version=2)
    ch_pc=random.randrange(1,3)
    v=visualize_choose(ch_pc)
    print("Ho scelto ", v , '\n')
    ris=compare_choose(ch_user, ch_pc)
    if(ris==0):
        print("Abbiamo pareggiato :| \n")
    elif(ris==1):
        print("Hai vinto :( \n")
        user_score+=1
    elif(ris==-1):
        print("Ho vinto :D \n")
        pc_score+=1
    
    print("Algoritmo:", pc_score , "\t Tu:" , user_score )

    print("Vuoi rigiocare? y/n ")
    s_regame=True
    while s_regame:
        regame=input()
        regame=regame.lower()
        if(regame!='y' and regame!='n'):
            print("Perfavore, devi inserire una y=yes o una n=no\n")
        else:
            s_regame=False
    if (regame=='n'):
        exit()
    
    partita+=1



    








    
    



