from main import VBk

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