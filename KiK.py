import os
import random
import time 
def wypisz(x,znak,znak2):
    print("       |       |                    ",end='')
    if znak!='' and znak2!='': 
        print(" Grasz jako: ",znak," , ","Przeciwnik: ",znak2)
    else:
        print("")  
    print("  ",x[0],"  |  ",x[1],"  |  ",x[2])
    print("       |       |       ")
    print("-----------------------")
    print("       |       |       ")
    print("  ",x[3],"  |  ",x[4],"  |  ",x[5])
    print("       |       |       ")
    print("-----------------------")
    print("       |       |       ")
    print("  ",x[6],"  |  ",x[7],"  |  ",x[8])
    print("       |       |       \n")
def sprawdz_miejsce(x,y):
    if x[y]==" ":
        return True
    return False
def ruch_komputera(x,znak,znak2,i,level):
    RUCHY_DEFAULT=(4,0,2,6,8,1,5,7,3)
    losowa=0 
    if level==False:
       if i<2:
            losowa=random.randint(0,8)
            if x[losowa]==" ":
                return losowa
    elif level==True:
       if x[4]==" ":
            return 4
       elif i==1:
            losowa=random.randint(1,8)
            if x[losowa]==" ":
                 return losowa     
    for k in range(0,9,3):
            if x[k]==znak2 and x[k+1]==znak2:
                if x[k+2]==" ":
                    return k+2
            if x[k+1]==znak2 and x[k+2]==znak2:
                if x[k]==" ":
                    return k
            if x[k]==znak2 and x[k+2]==znak2:
                if x[k+1]==" ":
                    return k+1            
    for a in range(3):
            if x[a]==znak2 and x[a+3]==znak2:
                if x[a+6]==" ":
                    return a+6
            if x[a+3]==znak2 and x[a+6]==znak2:
                if x[a]==" ":
                    return a
            if x[a]==znak2 and x[a+6]==znak2:
                if x[a+3]==" ":
                    return a+3             
    for a in range(0,4,2):
            if x[a]==znak2 and x[4]==znak2:
                if x[a+8-a*2]==" ":
                    return a+8-a*2
            if x[4]==znak2 and x[a+8-a*2]==znak2:
                if x[a]==" ":
                    return a
            if x[a]==znak2 and x[a+8-a*2]==znak2:
                if x[4]==" ":
                    return 4          
    for k in range(0,9,3):
            if x[k]==znak and x[k+1]==znak:
                if x[k+2]==" ":
                    return k+2
            if x[k+1]==znak and x[k+2]==znak:
                if x[k]==" ":
                    return k
            if x[k]==znak and x[k+2]==znak:
                if x[k+1]==" ":
                    return k+1 
    for a in range(3):
            if x[a]==znak and x[a+3]==znak:
                if x[a+6]==" ":
                    return a+6
            if x[a+3]==znak and x[a+6]==znak:
                if x[a]==" ":
                    return a
            if x[a]==znak and x[a+6]==znak:
                if x[a+3]==" ":
                    return a+3
    for a in range(0,4,2):
            if x[a]==znak and x[4]==znak:
                if x[a+8-a*2]==" ":
                    return a+8-a*2
            if x[4]==znak and x[a+8-a*2]==znak:
                if x[a]==" ":
                    return a
            if x[a]==znak and x[a+8-a*2]==znak:
                if x[4]==" ":
                    return 4                             
    for k in range(0,9,3):
            if x[k]==" " and x[k+1]==" ":
                if x[k+2]==" ":
                    return k+2
            if x[k+1]==" " and x[k+2]==" ":
                if x[k]==" ":
                    return k
            if x[k]==" " and x[k+2]==" ":
                if x[k+1]==" ":
                    return k+1
    for a in range(3):
            if x[a]==" " and x[a+3]==" ":
                if x[a+6]==" ":
                    return a+6
            if x[a+3]==" " and x[a+6]==" ":
                if x[a]==" ":
                    return a
            if x[a]==" " and x[a+6]==" ":
                if x[a+3]==" ":
                    return a+3
    for a in range(0,4,2):
            if x[a]==" " and x[4]==" ":
                if x[a+8-a*2]==" ":
                    return a+8-a*2
            if x[4]==" " and x[a+8-a*2]==" ":
                if x[a]==" ":
                    return a
            if x[a]==" " and x[a+8-a*2]==" ":
                if x[4]==" ":
                    return 4
    while True:
            losowa=random.randint(0,8)
            if x[losowa]==" ":
                return losowa   
def sprawdz(x,znak,znak2):
     for k in range(0,9,3):
           if x[k]==znak and x[k+1]==znak and x[k+2]==znak:
                print("Wygral: ",znak)
                return True
           elif x[k]==znak2 and x[k+1]==znak2 and x[k+2]==znak2:
                print("Wygral: ",znak2)
                return True 
     for k in range(3):
           if x[k]==znak and x[k+3]==znak and x[k+6]==znak:
                print("Wygral: ",znak)
                return True
           elif x[k]==znak2 and x[k+3]==znak2 and x[k+6]==znak2:
                print("Wygral: ",znak2)
                return True
     for a in range(0,4,2):
            if x[a]==znak and x[4]==znak and x[a+8-a*2]==znak:
                 print("Wygral: ",znak)
                 return True                
            elif x[a]==znak2 and x[4]==znak2 and x[a+8-a*2]==znak2:
                 print("Wygral: ",znak2)   
                 return True
     i=0
     while i<len(x):
        if x[i]==" ":
            break;
        i+=1
     if i==len(x):
        print("Remis!")
        return True    
     return False                                
pozycje=["0","1","2","3","4","5","6","7","8"]
print("Witaj w Grze Kolko i Krzyzyk!\n")
print("Sprobuj swoich sil w starciu z komputerem")
print("Plansza zostala ponumerowana w nastepujacy sposob\n")
wypisz(pozycje,'','')
print("\nAby grac wybierz z klawiatury cyfre pola na ktorym chcialbys\chcialabys umiescic X\O")
print("Milej zabawy!")
os.system("PAUSE")
os.system("cls")
pozycje.clear()     
while True:
    for x in range(9):
        pozycje.append(" ")
    start_Player=False
    buf,poziom_trudnosci,i,znak_komp,znak2,znak=False,False,0,"","",0
    while znak2=="" and znak_komp=="":
        wypisz(pozycje,'','')
        print("1.Kolko O")
        print("2.Krzyzyk X\n")    
        znak=int(input("Kolko czy krzyzyk\n"))
        if znak==1:
            znak2='O'
            znak_komp='X'
        elif znak==2:
            znak2='X'
            znak_komp='O'
        else:
            print("Nie ma takiego znaku\n")
            os.system("PAUSE")
            os.system("cls")
    os.system("cls")
    while True:
        wypisz(pozycje,znak2,znak_komp)
        print("Wybierz poziom trudnosci")
        print("1.Latwy")
        print("2.Trudny")
        znak=int(input(""))
        if znak==1:
            break
        elif znak==2:
           poziom_trudnosci=True
           break
        else:
            print("Nie ma takiej opcji\n")
            os.system("PAUSE")
            os.system("cls") 
    os.system("cls")    
    while True:
        wypisz(pozycje,znak2,znak_komp)
        print("Kto zaczyna?")
        print("1.Kolko O")
        print("2.Krzyzyk X\n")
        znak=int(input("Kolko czy krzyzyk\n"))
        if znak==1:
            if znak2=='O':
                start_Player=True
            break;
        elif znak==2:
             if znak2=='X':
                start_Player=True
             break;
        else:
             print("Nie ma takiego znaku\n")
             os.system("PAUSE")
             os.system("cls")    
    os.system("cls")
    wypisz(pozycje,znak2,znak_komp)
    while buf==False and i<9:
        if start_Player==True and i<9:
            while buf==False:    
                Player=int(input("Podaj pozycje od 0-8\n"))
                buf=sprawdz_miejsce(pozycje,Player)
                if buf==False:
                    print("pozycja: ",Player," jest zajeta")
                    os.system("PAUSE")
                    os.system("cls")
                    wypisz(pozycje,znak2,znak_komp)
                else:     
                    pozycje[Player]=znak2
                    i+=1
                    os.system("cls")
                    wypisz(pozycje,znak2,znak_komp)
        if sprawdz(pozycje,znak2,znak_komp)==True:
                break;
        if i<9:
            pozycje[ruch_komputera(pozycje,znak2,znak_komp,i,poziom_trudnosci)]=znak_komp
            print("Mysle...")
            time.sleep(1)
            i+=1
        os.system("cls")
        wypisz(pozycje,znak2,znak_komp)
        buf=sprawdz(pozycje,znak2,znak_komp)
        start_Player=True
    buf=False
    os.system("PAUSE")
    os.system("cls")
    pozycje.clear()    
        
