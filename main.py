class VBk:
    lista = []
    def __init__(self, sor, csapat, hely, vbev, vbhely):
        self.sorszam = sor
        self.orszag = csapat
        self.helyezes = hely
        self.ev = vbev
        self.hely = vbhely
        VBk.lista.append(self)
    
with open("input.txt","r",encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split("\t")
        t = VBk(int(s[0]), s[1], int(s[2]), int(s[3]), s[4])

#GÁBOR#

# 1-6

def helyezés(lista, bekertorszag):
    i = 0
    
    while i<len(lista):
        if (lista[i].orszag==bekertorszag):
            print(lista[i].helyezes, ", ", lista[i].ev, ", ", lista[i].hely )

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
            print(lista[i].orszag)
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

###

#BALU#

with open("input.txt","r",encoding="utf8") as f:
	for sor in f:
		s = sor.strip().split("\t")
		t = VBk(int(s[0]), s[1], int(s[2]), int(s[3]), s[4])

def Döntőkikapásokszáma(ország):
    hanyszorkapottki = 0
    for vbk in VBk.lista:
        if (vbk.helyezes == 2 and vbk.orszag == ország):
            hanyszorkapottki+=1
    print (f"{ország} {hanyszorkapottki}-szer/ször/szor kapott ki a döntőben")

def Kinyertakkor(évszám):
    for vbk in VBk.lista:
        if (vbk.ev == évszám and vbk.helyezes == 1):
            print(f"{évszám}-ban/ben {vbk.orszag} nyert!")

def LegkorábbiVB():
    legkorábbi = VBk.lista[0].ev
    for vbk in VBk.lista:
        if (vbk.ev < legkorábbi):
            legkorábbi = vbk.ev
    print(legkorábbi)

def HányszornyertVBt(ország):
    ennyiszernyert = 0
    for vbk in VBk.lista:
        if (vbk.helyezes == 1 and vbk.orszag == ország):
            ennyiszernyert+=1
    print(f"{ország} {ennyiszernyert}-szor/szer nyert VB-t")

def Mialegjobbhelyezés(ország):
    legjobbhely = -1
    for vbk in VBk.lista:
        if ((legjobbhely == -1 or legjobbhely > vbk.helyezes) and vbk.orszag == ország):
            legjobbhely = vbk.helyezes
    print(f"{legjobbhely}. helyezés volt {ország}-nak/nek eddig a legjobbja" if (not legjobbhely == -1) else f"{ország}-nak/nek nem volt helyezése a VB-n")

print("24) Hányszor kapott ki a döntőben Magyarország?")
Döntőkikapásokszáma("Magyarország")

print("25) Hányszor kapott ki a döntőben Mongólia?")
Döntőkikapásokszáma("Mongólia")

print("26) Hányszor kapott ki a döntőben Svájc?")
Döntőkikapásokszáma("Svájc")

print("27) Hányszor kapott ki a döntőben Brazília?")
Döntőkikapásokszáma("Brazília")

print("28) Hányszor kapott ki a döntőben Németország?")
Döntőkikapásokszáma("Németország")

print("29) Hányszor kapott ki a döntőben Argentína?")
Döntőkikapásokszáma("Argentína")

print("30)")
Kinyertakkor(1994)

print("31)")
LegkorábbiVB()

print("32) Magyarország hányszor nyert vb-t?")
HányszornyertVBt("Magyarország")

print("33) Anglia hányszor nyert vb-t?")
HányszornyertVBt("Anglia")

print("34) Chile hányszor nyert vb-t?")
HányszornyertVBt("Chile")

print("35) Peru hányszor nyert vb-t?")
HányszornyertVBt("Peru")

print("36) Mongólia hányszor nyert vb-t?")
HányszornyertVBt("Mongólia")

print("37) Írd ki Magyarország vb-n elért legjobb helyezését!")
Mialegjobbhelyezés("Magyarország")

print("38) Írd ki Anglia vb-n elért legjobb helyezését!")
Mialegjobbhelyezés("Anglia")

print("39) Írd ki Chile vb-n elért legjobb helyezését!")
Mialegjobbhelyezés("Chile")

print("40) Írd ki Peru vb-n elért legjobb helyezését!")
Mialegjobbhelyezés("Peru")

print("41) Írd ki Mongólia vb-n elért legjobb helyezését!")
Mialegjobbhelyezés("Mongólia")

###

#NIKI#

def LegHely(lista, orszag):    
    i = 0
    while i< len(lista) and not lista[i].orszag == orszag:
        i+=1
    leg = lista[i].helyezes
    for elem in lista:
        if elem.orszag == orszag and elem.helyezes < leg:
            leg = elem.helyezes
    print(leg)

def HanyVB(lista, orszag):
    vbcimek = 0
    for elem in lista:
        if elem.orszag == orszag and elem.helyezes == 1:
            vbcimek+=1
    print(vbcimek)

def KiNyert(lista, rendezo):
    szotar = {}
    voltVB = False
    for elem in lista:
        if elem.hely == rendezo and elem.helyezes == 1:
            if elem.orszag in szotar.keys():
                szotar[elem.orszag] +=1
            else:
                szotar[elem.orszag] = 1
                voltVB = True
    for orszag, amount in szotar.items():
        print("{}: {}".format(orszag, amount))
    if not voltVB: print("Ebben az országban nem volt VB rendezve")

def Helyszin(lista, input):
    for elem in lista:
        if elem.helyezes == 1 and elem.hely == input:
            print(f"{elem.orszag} - {elem.ev}")

def DobNyert(lista, dobogos):
    nyertesek = {}
    for elem in lista:
        if elem.helyezes == 1:
            if elem.orszag in nyertesek.keys():
                nyertesek[elem.ev] = elem.orszag
            else:
                nyertesek[elem.ev] = elem.orszag
        if elem.orszag == dobogos and (elem.helyezes == 1 or elem.helyezes == 2 or elem.helyezes == 3):
            print(nyertesek[elem.ev])

def Donto(lista, orszag):
    evek = []
    for elem in lista:
        if elem.orszag == orszag and (elem.helyezes == 1 or elem.helyezes == 2):
            evek.append(elem.ev)
    i = 0
    if not len(evek) == 0: 
        while i < len(lista) and not len(evek) == 0:
            if lista[i].ev == evek[0] and not lista[i].orszag == orszag:
                print(f"{lista[i].orszag} - {evek[0]}")
                evek.remove(evek[0])
            i+=1
    else: print("Ez az ország nem játszott döntőt.")

def Tobb(lista, nyertEkellE):
    tobb = {1:[], 2:[]}
    for elem in lista:
        if nyertEkellE:
            if elem.helyezes == 1:
                if elem.orszag in tobb[1] and elem.orszag not in tobb[2]:
                    tobb[2] += [elem.orszag]                    
                else:
                    tobb[1] += [elem.orszag]
        else:
            if elem.helyezes == 1: #azért, hogy ne írja adjon hozzá az összes résztvevőnél
                if elem.hely in tobb[1] and elem.hely not in tobb[2]:
                    tobb[2] += [elem.hely]
                else:
                    tobb[1] += [elem.hely]
    for value in tobb[2]:
        print(value)

def LegOrsz(lista, filt):
    stat = {}
    for elem in lista:
        if filt(elem):
            if elem.orszag in stat.keys(): stat[elem.orszag] +=1
            else: stat[elem.orszag] = 1

    mxV = max(stat.items(), key=lambda x: x[1])
    keyD = {}
    for key, value in stat.items():
        if value == mxV[1]:
            keyD[key] = value
    PrintDict(keyD)
    
def LegRend(lista, filt):
    stat = {}
    for elem in lista:
        if filt(elem):
            if elem.hely in stat.keys(): stat[elem.hely] +=1
            else: stat[elem.hely] = 1

    mxV = max(stat.items(), key=lambda x: x[1])
    keyD = {}
    for key, value in stat.items():
        if value == mxV[1]:
            keyD[key] = value
    PrintDict(keyD)

def PrintDict(dict):
    for k,v in dict.items():
        print(f"{k}: {v}")


print("42)	A program olvasson be egy csapat nevet és írja ki, a csapat vb-n elért legjobb helyezését!")
inp = input("Írd be egy ország nevét:  ")
LegHely(VBk.lista, inp)

print("43)	A program olvasson be egy csapat nevet és írja ki, a csapat hányszor nyert vb-t!")
inp = input("Írd be egy ország nevét:  ")
HanyVB(VBk.lista, inp)

print("44)	Melyik csapatok nyertek az Angiában rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!")
KiNyert(VBk.lista, "Anglia")
print("45)	Melyik csapatok nyertek a Magyarországon rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!")
KiNyert(VBk.lista, "Magyarország")
print("46)	Melyik csapatok nyertek a Németországban rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!")
KiNyert(VBk.lista, "Németország")
print("47)	Melyik csapatok nyertek az Brazíliában rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!")
KiNyert(VBk.lista, "Brazília")
print("48)	Melyik csapatok nyertek az Egyesült Államok rendezett vb-ken? A csapatok neve mellett az évszámot is írja ki!")
KiNyert(VBk.lista, "Egyesült Államok")

print("49)	A program olvasson be egy ország nevet és írja ki, melyik csapatok nyertek az adott helyszínen! A csapatok neve mellett az évszámot is írja ki!")
inp = input("Írd be egy ország nevét:  ")
Helyszin(VBk.lista, inp)

print("50)	Melyik csapat nyerte a vb-t, amikor Magyarország dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!")
DobNyert(VBk.lista, "Magyarország")
print("51)	Melyik csapat nyerte a vb-t, amikor Brazília dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!")
DobNyert(VBk.lista, "Brazília")
print("52)	Melyik csapat nyerte a vb-t, amikor Argentína dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!")
DobNyert(VBk.lista, "Argentína")

print("53)	Kikkel játszott döntőt Magyarország? Az ellenfél csapat neve mellett az évszámot is írja ki!")
Donto(VBk.lista, "Magyarország")
print("54)	Kikkel játszott döntőt Mongólia? Az ellenfél csapat neve mellett az évszámot is írja ki!")
Donto(VBk.lista, "Mongólia")
print("55)	Kikkel játszott döntőt Svájc? Az ellenfél csapat neve mellett az évszámot is írja ki!")
Donto(VBk.lista, "Svájc")
print("56)	Kikkel játszott döntőt Barzília? Az ellenfél csapat neve mellett az évszámot is írja ki!")
Donto(VBk.lista, "Brazília")
print("57)	A program olvasson be egy ország nevet és írja ki, kikkel játszott döntőt az illető csapat? Az ellenfél csapat neve mellett az évszámot is írja ki!")
inp = input("Írd be egy ország nevét:  ")
Donto(VBk.lista, inp)

print("58)	Melyik csapat nyert többször is vb-t?")
Tobb(VBk.lista, True)
print("59)	Melyik országban rendeztek többször is vb-t?")
Tobb(VBk.lista, False)

print("60)	Melyik csapat(ok) nyert a legtöbbször vb-t? A csapat neve mellett a vb gyözelmmek számát is írja ki! ")
LegOrsz(VBk.lista, lambda x: x.helyezes == 1)

print("61)	Melyik ország(ok) rendezett legtöbbször vb-t? A csapat neve mellett a vb-k számát is írja ki! ")
LegRend(VBk.lista, lambda x: x.helyezes == 1)

print("62)	Melyik csapat(ok) kapott ki a legtöbbször a döntőben? A csapat neve mellett a vereségek számát is írja ki!")
LegOrsz(VBk.lista, lambda x: x.helyezes == 2)

###