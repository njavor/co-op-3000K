class VBk:
    lista = []
    def __init__(self, sor, csapat, hely, vbev, vbhely):
        self.sorszam = sor
        self.orszag = csapat
        self.helyezes = hely
        self.ev = vbev
        self.hely = vbhely
        VBk.lista.append(self)