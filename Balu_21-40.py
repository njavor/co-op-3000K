from operator import le
from main import VBk

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