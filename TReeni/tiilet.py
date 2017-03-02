'''Tämä on se missä pelaaja kävelee, X-Y kordinaatteja käyttäen'''
import tavarat, vastustajat

class KarttaRuutu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
'''Kun joku pelaaja astuu karttaruutuun, tämä tapahtuu'''
def intro_teksti(self):
    raise NotImplementedError()

def muokkaa_pelaajaa(self, pelaaja
    raise NotImplementedError()

'''Aloitushuone'''

class AloitusHuone(KarttaRuutu):
    def intro_teksti(self):
        return """
    Löydät itsesi kaivoksesta jossa on värähtelevä lamppu seinässä.
    Voit valita neljästä reitistä, jokainen niistä on yhtä pimeä ja pelottava.
    """
    
    def muokkaa_pelaajaa(self, pelaaja):
        #Huoneessa ei ole tehtävää pelaajalle...
        pass
    
class LoytoHuone(KarttaRuutu):
    def __init__(self, x, y, tavarat):
        self.tavarat = tavarat
        super().__init__(x, y)
        
    def lisaa_loydot(self, pelaaja):
        player.inventory.append(self.tavarat)
        
    def muokkaa_pelaajaa(self, pelaaja):
        self.lisaa_loydot(pelaaja)
        
class VastustajaHuone(KarttaRuutu):
    def __init__(self, x, y, vastustajat):
        self.vastustajat = vastustajat
        super().__init__(x, y)
        
    def muokkaa_pelaajaa(self, itse_pelaaja):
        if self.vastustaja.on.elossa():
            itse_pelaaja.elamapisteet = itse_pelaaja.elamapisteet - self.vastustajat.vahinko
            print("Vastustaja tekee {} vahinkoa. Sinulla on {} elämäpisteitä jäljellä.".format(self.vastustajat.vahinko, itse_pelaaja.elamapisteet))

class TyhjaKaytavaReitti(KarttaRuutu):
    def intro_teksti(self):
        return """
        Toinen kohta kaivosta... Sinun on pakko edetä.
        """
        
    def muokkaa_pelaajaa(self, player):
        #Huoneessa ei oo mitään tekemistä pelaajalle.. vielä
        pass
    
class FatisagHuone(VastustajaHuone):
    def __init__(self, x, y):
        super().__init__(x, y, vastustajat.FatisagNiko())
    
    def intro_teksti(self):
        if self.vastustaja.on.elossa():
            return """
            Jättimäinen Niko hyppää sinun päällesi edessäsi!
            """
            
        else:
            return """
            Kuollut Niko makaa maassa ja homehtuu.
            """
            
class MoraLoytoHuone(LoytoHuone):
    def __init__(self, x, y):
        super().__init__(x, y, tavarat.mora())
        
    def intro_teksti(self):
        return """
        Löydät jotain hienoa sivusta...
        Se on mora! Nostat sen ylös.            
            """
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            