import pelaaja
from TReeni.vastustajat import Vastustaja

class Toiminto():
    def __init__(self, metodi, nimi, pikanappain, **kwargs):
        self.metodi = metodi
        self.pikanappain = pikanappain
        self.nimi = nimi
        self.kwargs = kwargs
        
    
    def __str__(self):
        return "{}: {}".format(self.pikanappain, self.nimi)
    
class MoveNorth(Toiminto):
    def __init__(self):
        super().__init__(metodi=pelaaja.move_north, nimi='Liiku pohjoiseen', pikanappain='n')
 
 
class MoveSouth(Toiminto):
    def __init__(self):
        super().__init__(metodi=pelaaja.move_south, nimi='Liiku etelään', pikanappain='s')
 
 
class MoveEast(Toiminto):
    def __init__(self):
        super().__init__(metodi=pelaaja.move_east, nimi='Liiku itään', pikanappain='e')
 
 
class MoveWest(Toiminto):
    def __init__(self):
        super().__init__(metodi=pelaaja.move_west, nimi='Liiku länteen', pikanappain='w')
 
 
class KatsoVarusteluettelo(Toiminto):
    """Näyttää pelaajan varusteluettelon"""
    def __init__(self):
        super().__init__(metodi=pelaaja.print_inventory, nimi='Katso varusteluettelo', pikanappain='i')
        
        
class Hyokkays(Toiminto):
    def __init__(self, enemy):
        super().__init__(metodi=pelaaja.attack, nimi="Hyökkää", pikanappain='a', Vastustaja=Vastustaja)
        
class Karkaa(Toiminto):
    def __init__(self, tile):
        super().__init__(method=pelaaja.flee, nimi="Karkaa", pikanappain='f', tile=tile)
        