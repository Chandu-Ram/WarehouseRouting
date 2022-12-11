from math import hypot
from random import shuffle

class Itemloc:
    def __init__(self, name: str, coords: tuple):
        self._name = name
        self._x, self._y = coords

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @staticmethod
    def distance(item1, item2):
        return hypot(item2.x - item1.x, item2.y - item1.y)

    def __repr__(self):
        return f'{self._name}'


class Item:
    def __init__(self):
        self._items = []

    def add(self, x):
        if isinstance(x, list):
            self.items.extend(x)
        elif isinstance(x, Itemloc):
            self.items.append(x)
        else:
            assert False, "Wrong type"

    @property
    def items(self):
        return self._items


class Route:
    def __init__(self, items, shuffled=False):
        self._genes = items[:]
        if not shuffled:
            shuffle(self._genes)
        self._fitness = None
        self.chance = None

    @property
    def fitness(self):
        distances = (Itemloc.distance(self._genes[i], self._genes[i + 1]) for i in range(-1, len(self._genes) - 1))
        self._fitness = 10 / sum(distances)
        return self._fitness

    @property
    def raw_fitness(self):
        return self._fitness

    @property
    def genes(self):
        return self._genes

    def copy(self):
        clone = Route(self._genes, shuffled=True)
        clone._fitness = self.raw_fitness
        clone.chance = None
        return clone

    def __repr__(self):
        return f'<Route ({self._fitness})>'

    def __str__(self):
        return '->'.join(repr(item) for item in self._genes)

