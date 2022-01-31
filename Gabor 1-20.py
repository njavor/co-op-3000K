"""
1)	Írja ki Magyarország által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.
2)	Írja ki Anglia által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.
3)	Írja ki Chile által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.
4)	Írja ki Peru által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.
5)	Írja ki Mongólia által elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.
6)	A program olvasson be egy csapat nevet és írja ki a csapat álta elért helyezéseket. A kiírásban jelenjen meg a vb éve és helyszíne is.
7)	A program írja ki, hogy az '30-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.
8)	A program írja ki, hogy az '40-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.
9)	A program írja ki, hogy az '50-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.
10)	A program írja ki, hogy az '60-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.
11)	A program írja ki, hogy az '70-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.
12)	A program írja ki, hogy az '80-es években kik lettek a világbajnokok! Az ország neve mellett szerepeljen az évszám is.
13)	Írja ki Magyarország hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!
14)	Írja ki Anglia hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!
15)	Írja ki Chile hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!
16)	Írja ki Peru hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!
17)	Írja ki Mongólia hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!
18)	A program olvasson be egy csapat nevet és írja ki, a csapat hányszor jutott ki a vb-re a fájl által tartalmazott időszakban!
19)	Melyik csapat nyert 1930-ban?
20)	Melyik csapat nyert 1940-ben?
"""

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
        if(lista[i].ev[2]==évek):
            print(lista[i].orszag, ",", lista[i].ev)

        i+=1
