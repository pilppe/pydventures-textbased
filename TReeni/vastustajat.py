'''Vastustajat:
FatisagNiko
JesseJ

Tehty 02.03.2017
'''

class Vastustaja:
    def __init__(self, nimi, elamapisteet, vahinko):
        self.nimi = nimi
        self.elamapisteet = elamapisteet
        self.vahinko = vahinko
        
def onko_elossa(self):
    return self.elamapisteet > 0

class FatisagNiko(Vastustaja):
    def __init__(self):
        super().__init__(nimi="Fätisäg Niko", elamapisteet=15, vahinko=2)
        
class JesseJ(Vastustaja):
    def __init__(self):
        super().__init__(nimi="Jessie J", elamapisteet=30, vahinko=15)
        
class antti_Kaskimaki(Vastustaja):
    def __init__(self):
        super().__init__(nimi="Antti Kaskimäki", elamapisteet=50, vahinko=20)

