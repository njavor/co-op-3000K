from main import VBk

def KiNyert(lista, rendezo):
    szotar = {}
    for elem in lista:
        if elem.hely == rendezo and elem.helyezes == 1:
            if elem.orszag in szotar.keys():
                szotar[elem.orszag] +=1
            else:
                szotar[elem.orszag] = 1
    print(szotar)

print("42)	A program olvasson be egy csapat nevet és írja ki, a csapat vb-n elért legjobb helyezését!")
print("43)	A program olvasson be egy csapat nevet és írja ki, a csapat hányszor nyert vb-t!")
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
print("50)	Melyik csapat nyerte a vb-t, amikor Magyarország dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!")
print("51)	Melyik csapat nyerte a vb-t, amikor Brazília dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!")
print("52)	Melyik csapat nyerte a vb-t, amikor Argentína dobogós helyzést ért el? A győzetes csapatok neve mellett az évszámot is írja ki!")
print("53)	Kikkel játszott döntőt Magyarország? Az ellenfél csapat neve mellett az évszámot is írja ki!")
print("54)	Kikkel játszott döntőt Mongólia? Az ellenfél csapat neve mellett az évszámot is írja ki!")
print("55)	Kikkel játszott döntőt Svájc? Az ellenfél csapat neve mellett az évszámot is írja ki!")
print("56)	Kikkel játszott döntőt Barzília? Az ellenfél csapat neve mellett az évszámot is írja ki!")
print("57)	A program olvasson be egy ország nevet és írja ki, kikkel játszott döntőt az illető csapat? Az ellenfél csapat neve mellett az évszámot is írja ki!")
print("58)	Melyik csapat nyert többször is vb-t?")
print("59)	Melyik országban rendeztek többször is vb-t?")
print("60)	Melyik csapat(ok) nyert a legtöbbször vb-t? A csapat neve mellett a vb gyözelmmek számát is írja ki! ")
print("61)	Melyik ország(ok) rendezett legtöbbször vb-t? A csapat neve mellett a vb-k számát is írja ki! ")
print("62)	Melyik csapat(ok) kapott ki a legtöbbször a döntőben? A csapat neve mellett a vereségek számát is írja ki!")