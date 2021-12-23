import random
import os

i={

}

def ip():

    r = random.randint(0, 256)
    rr = random.randint(0, 256)
    rrr = random.randint(0, 256)   
    rrrr = random.randint(0, 256)
    return str(r)+"."+str(rr)+"."+str(rrr)+"."+str(rrrr)

ip()

def mac(length):
    r1 = ''.join(random.choice('A''B''C''D''1''2''3''4''5''6''7''8''9') for i in range(length))
    r2 = ''.join(random.choice('A''B''C''D''1''2''3''4''5''6''7''8''9') for i in range(length))
    r3 = ''.join(random.choice('A''B''C''D''1''2''3''4''5''6''7''8''9') for i in range(length))
    r4 = ''.join(random.choice('A''B''C''D''1''2''3''4''5''6''7''8''9') for i in range(length))
    r5 = ''.join(random.choice('A''B''C''D''1''2''3''4''5''6''7''8''9') for i in range(length))
    r6 = ''.join(random.choice('A''B''C''D''1''2''3''4''5''6''7''8''9') for i in range(length))
    return str(r1)+":"+str(r2)+":"+str(r3)+":"+str(r4)+":"+str(r5)+":"+str(r6)

def da():
    a=0
    m=1
    while a!="0":
        a=input("Add meg az  "+ str(m) +". számitógép nevét: ")
        os.system("cls")
        i[m]={}
        i[m]['nev:']= a
        i[m]['ip cim: ']=ip()
        i[m]['mac cim: ']=mac(2)
        i[m]['------']=""

        m+=1

da()

def ki():
    da()
    for kulcs,adat, in i.items():
        print(kulcs,adat)
ki()