import string
from main import VBk

 # 1-6

def helyezés(lista, bekertorszag):
    i = 0
    
    while i<len(lista):
        if (lista[i].orszag==bekertorszag):
            print (lista[i].helyezes, ", ", lista[i].ev, ", ", lista[i].hely )

        i+=1


# 7-12

def bajnokok(lista, évek):
    i =0
    while i<len(lista):
      
        if(str(lista[i].ev)[2]==évek):
            print(lista[i].orszag, ", ", lista[i].ev)

        i+=1

# 13-18

def vb_szereplések (lista, bekertorszag):
    számláló=0
    for elem in lista:
        if elem.orszag==bekertorszag:
            számláló+=1
    
    print (számláló)

# 19-23
def nyertes(lista, éve):
    i=0
    while(i<len(lista)):
        if str(lista[i].ev)==éve and str(lista[i].helyezes)=="1":
            print (lista[i].orszag)
        i+=1


print("1)	Írja ki Magyarország által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
helyezés(VBk.lista, "Magyarország")

print("2)	Írja ki Anglia által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
helyezés(VBk.lista, "Anglia")

print("3)	Írja ki Chile által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
helyezés(VBk.lista, "Chile")

print("4)	Írja ki Peru által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
helyezés(VBk.lista, "Peru")

print("5)	Írja ki Mongólia által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
helyezés(VBk.lista, "Mongólia")

print("6)	A program olvasson be egy csapat nevet és írja ki a csapat álta elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.")
orszagkérés =input()
helyezés(VBk.lista, orszagkérés)

print("7)	A program írja ki, hogy az '30-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")
bajnokok(VBk.lista, "3")

print("8)	A program írja ki, hogy az '40-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")
bajnokok(VBk.lista, "4")

print("9)	A program írja ki, hogy az '50-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")
bajnokok(VBk.lista, "5")

print("10)	A program írja ki, hogy az '60-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")
bajnokok(VBk.lista, "6")

print("11)	A program írja ki, hogy az '70-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")
bajnokok(VBk.lista, "7")

print("12)	A program írja ki, hogy az '80-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.")
bajnokok(VBk.lista, "8")

print("13)	Írja ki Magyarország hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!")
vb_szereplések(VBk.lista, "Magyarország")

print("14)	Írja ki Anglia hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!")
vb_szereplések(VBk.lista, "Anglia")

print("15)	Írja ki Chile hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!")
vb_szereplések(VBk.lista, "Chile")

print("16)	Írja ki Peru hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!")
vb_szereplések(VBk.lista, "Peru")

print("17)	Írja ki Mongólia hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!")
vb_szereplések(VBk.lista, "Mongólia")

print("18)	A program olvasson be egy csapat nevet és írja ki, a csapat hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!")
orszagkérés2=input()
vb_szereplések(VBk.lista, orszagkérés2)

print("19)	Melyik csapat nyert 1930-ban?")
nyertes(VBk.lista,"1930")

print("20)	Melyik csapat nyert 1940-ben?")
nyertes(VBk.lista,"1940")

print("21)	Melyik csapat nyert 1950-ben?")
nyertes(VBk.lista,"1950")

print("22)	Melyik csapat nyert 1960-ban?")
nyertes(VBk.lista,"1960")

print("23)	Melyik csapat nyert 1970-ben?")
nyertes(VBk.lista,"1970")

