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