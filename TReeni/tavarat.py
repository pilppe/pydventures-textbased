
'''Superclass = Tavarat'''


class Tavarat():
    '''Alkuperäinen koodi tavaroille'''
    def __init__(self, nimi, kuvaus, arvo):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.arvo = arvo


def __str__(self):
    return "{}\n=====\n{}Arvo: {}\n".format(self.nimi, self.kuvaus, self.value)

'''Aseet'''


class Kulta():
    def __init__(self, amt):
        self.amt = amt
        super().__init__(nimi="Kulta",
                         kuvaus="Pyöreä kolikko missä lukee {} edessä.".format(str(self.amt)),
                         value=self.amt)


class Ase(Tavarat):
    def __init__(self, nimi, kuvaus, arvo, vahinko):
        self.vahinko = vahinko
        super().__init__(nimi, kuvaus, arvo)

    def __str__(self):
        return "{}\n=====\n{}nArvo: {}\nVahinko: {}".format(self.nimi, self.kuvaus, self.arvo, self.vahinko)   


class kiminServaus(Ase):
    def __init__(self):
        super().__init__(nimi="Kimin servaus",
                         kuvaus="Tuntuu vähän, mutta ei muuten tunnu missään."
                         arvo=0,
                         vahinko=5)


class Mora(Ase):
    def __init__(self):
        super().__init__(name="Mora",
                         kuvaus="Pieni puukko missä on vähän ruostetta. Sattuu aika paljon enemmän kuin Kimnin servaus.",
                         arvo=10,
                         vahinko=10)
