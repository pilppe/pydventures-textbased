import maailma
from pelaaja import Pelaaja
from TReeni.toiminnot import Toiminto


def play():
    maailma.load_tiles()
    pelaaja = Pelaaja()
    huone = maailma.tile_exists(pelaaja.location_x, pelaaja.location_y)
    print(huone.intro_teksti())
    while pelaaja.on_elossa() and not pelaaja.voitto:
        room = maailma.tile_exists(pelaaja.location_x, pelaaja.location_y)
        room.modify_player(pelaaja)
        # Katso uudestaan koska huone voi vaihtaa pelaajan tilaa
        if pelaaja.on_elossa() and not pelaaja.voitto:
            print("Päätä toiminto:\n")
            available_actions = huone.available_actions()
            for action in available_actions:
                print(Toiminto)
            action_input = input('Toiminto: ')
            for action in available_actions:
                if action_input == Toiminto.pikanappain:
                    pelaaja.do_action(action, **action.kwargs)
                    break


class KaivosHuonePoistuminen(KarttaRuutu):
    def intro_text(self):
        return """
        Näet auringonvaloa kaukaalta... Se kasvaa kun lähenet sitä...

        Pääsit ulos! Voitto on sinun!
        """

    def muokkaa_pelaajaa(self, pelaaja):
        pelaaja.voitto = True


if __name__ == "__main__":
    play()
