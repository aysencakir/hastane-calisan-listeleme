class hastane(object):
    isim=""
    sonEklenenPersonelNo=0
    personelNo=0

    def __init__(self,isim1):
        self.isim=isim1
        self.personelNo=self.sonEklenenPersonelNo+1
        hastane.sonEklenenPersonelNo=self.personelNo

    def personelGorevAl(self):
        pass

class doktor(hastane):
    def __init__(self,isim1):
        hastane.__init__(self,isim1)
    def personelGorevAl(self):
        
        print("Isim:",self.isim)
        print("Gorev:Doktor")
        print("Personel No:",self.personelNo)

class bashekim(hastane):
    def __init__(self,isim1):
        hastane.__init__(self,isim1)
    def personelGorevAl(self):
        print("Isim:",self.isim)
        print("Gorev:Bashekim")
        print("Personel No:",self.personelNo)

class muhasebeci(hastane):
    def __init__(self,isim1):
        hastane.__init__(self,isim1)
    def personelGorevAl(self):
       
        print("Isim:",self.isim)
        print("Gorev:Muhasebeci")
        print("Personel No:",self.personelNo)

calisanlar=[doktor("Aysen Cakir"),doktor("Metehan Cakir"),doktor("Miray Yilmaz"),doktor("Irem Oztekin"),
            doktor("Ece Akkaynak"),bashekim("Ali Kacmaz"),muhasebeci("Akif Yigit"),muhasebeci("Arda Karadag")]

for calisan in calisanlar:
    calisan.personelGorevAl()
    print(" ")

