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