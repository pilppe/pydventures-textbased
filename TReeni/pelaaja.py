import tavarat, random, maailma

class Pelaaja():
    def __init__(self):
        self.tavaraluettelo = [tavarat.Kulta(20), tavarat.kiminServaus()]
        self.elamapisteet = 100
        self.location_x, self.location_y = maailma.starting.position
        self.voitto = False
        
    def onko_elossa(self):
        return self.hp > 0
    
    def print_tavaraluettelo(self):
        for tavarat in self.tavaraluettelo:
            print(tavarat, '\n')
            
'''Liikkuminen'''
def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
    print(maailma.tile_exists(self.location_x, self.location_y).intro_teksti())
    
def move_north(self):
    self.move(dx=0, dy=-1)
    
def move_south(self):
    self.move(dx=0, dy=1)
    
def move_east(self):
    self.move(dx=1, dy=0)
    
def move_west(self):
    self.move(dx=-1, dy=0)
    
def attack(self, enemy):
    paras_ase = None
    max_vahinko = 0
    for i in self.tavaraluettelo:
        if isinstance(i, tavaraluettelo.Ase):
            if i.vahinko > max_vahinko:
                max_vahinko = i.vahinko
                paras_ase = i
                
    print("You use {} against {}!".format(paras_ase.nimi, vastustajat.nimi))
    vastustajat.elamapisteet -= paras_ase.vahinko
    if not Vastustaja.on_elossa():
        print("You killed {}!".format(vastustajat.nimi))
    else:
        print("{} elämäpisteet on {}.".format(vastustajat.nimi, vastustajat.elamapisteet))
        
def do_action(self, toiminto, **kwargs):
    toiminta_metodi = getattr(self, toiminta.metodi.__nimi__)
    if toiminta_metodi:
        toiminta_metodi(**kwargs)
 
    def flee(self, tile):
        """Liikuttaa pelaajaa randomisti eri kohtiin"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
    
    
    
    
    
    
    
    
    
    