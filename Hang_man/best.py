import os
import getpass
import random
import time
import sys
'''def py(best):
    for i in range(0,len(best)-1):
        if best[i]!=best[len(best)-i-1]:
            flag=False
        else :
            flag= True

    print(flag)
'''
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()
var=0
#for i in range(1,100000):
#print(("Enter the word \n"))
def main():
    print("Welcome To Hang-Man V2.0")
    print("Written By, Bright Dumadi Lesi")
    #time.sleep(5)
    total = 4
    i = 0
    k=0
    thin=['Polishing Scene','Finishing up','Generating words','Setting up things for you',]
    while i < total:
        progress(i, total, status=thin[i])
        time.sleep(1.5)
        i += 1

    f=open("words.txt","r")
    cont=f.readlines()
    cont=list(cont)
    q=random.randint(0,len(cont)-1)
    word=cont[q]
    word=word.lower()
    best=list(word)
    p=["_"]
    mess=[False]
    #print(word)
    lives= len(word)+1
    rem=len(word)
    for i in range(rem-2):
        p.append("_")
        mess.append(False)
    os.system('clear')
    count=0
    r=[]
    print("The word has {} letters ".format(lives-2))
    print(p)
    while(lives-2):
        flag=False
        print("Wrong letters: ", r)
        guess= input("Guess the letters of the word \n")
        for i in best:
            if(guess==i):
                print("You have guessed a letter correctly")
                if(mess[best.index(guess)]==False):
                    p[best.index(guess)]=guess
                    mess[best.index(guess)]=True
                else:
                    w=word.find(guess,best.index(guess)+1)
                    p[w]=guess
                    mess[w]=True
                print(p)
                count=count+1
                flag= True
                break

        if(count==rem-1):
            print("You have guessed the complete word Good Job!!!")
            break;
        if(flag):
            continue;
        else:
            r.append(guess)
            lives=lives-1
        print(p)
        if(lives-2==0):
            print("You Loose!!! ")
            print("The word was, ",word)
        else:
            print("You have {} lives left ".format(lives-2))

if __name__ == '__main__':
    main()

#py("accrobats stab orca")
