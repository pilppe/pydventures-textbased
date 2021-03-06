'''Käy läpi maailma.txt tiedoston'''
_maailma = {}
starting_position = (0, 0)


def load_tiles():
    with open('resources/world.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))  # Olettaa että kaikilla riveillä on saman verran tabeja
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')  # Windows käyttäjät joutuvat ehkä korvaamaan '\r\n'
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _maailma[(x, y)] = None if tile_name == '' else getattr(__import__('tiilet'), tile_name)(x, y)


def tile_exists(x, y):
    return _maailma.get((x, y))
