from TSP import *
from libs.GeneticAlgorithm import GeneticAlgorithm


def main():
    WareHouse = Item()
    WareHouse.add([
        Itemloc('Watch', (49,21)),
        Itemloc('Television', (46,19)),
        Itemloc('Bag', (55,19)),
        Itemloc('Book', (51,17)),
        Itemloc('Mobile', (58,25)),
        Itemloc('Laptop', (0,0)),
        Itemloc('Refrigerator', (62,15)),
        Itemloc('Air Conditioner', (53,14)),
        Itemloc('Pendrives', (28,21)),
        Itemloc('HDD', (46,24)),
        Itemloc('Flash card', (35,32)),
        Itemloc('Bottles', (22,22))
    ])
    print('Items:', end=' ')
    print(*(item for item in WareHouse.items), sep=', ')
    ga = GeneticAlgorithm(100, mutation_rate=0.5, ptype=Route, args=(WareHouse.items,))
    ga.run(seconds=10)
    fittest = ga.alltime_best
    best_fitness = fittest.fitness
    print('Best route:', fittest)
    print('Best fitness:', best_fitness)
    print('Generations:', ga.generation)


if __name__ == '__main__':
    main()
