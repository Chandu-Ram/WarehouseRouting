import pygame
from TSP import *
from libs.GeneticAlgorithm import GeneticAlgorithm


def map_items_onto_screen(items):
    for item in items:
        y = -int(150 * (item.x - 54))
        x = int(50 * (item.y - 13.5))
        yield (x, y)


def text_labels(items, population_size, mutation_rate):
    global arial_norm, arial_small
    arial_norm = pygame.font.SysFont('arial', 25)
    arial_small = pygame.font.SysFont('arial', 16)
    labels = []
    for item, (posx, posy) in zip(items, map_items_onto_screen(items)):
        labels.append((arial_norm.render(item.name, 1, (255, 255, 255)), (posx - 45, posy - 15)))
    labels.append((arial_small.render('Population size: {}'.format(population_size), 1, (255, 255, 255)), (450, 10)))
    labels.append((arial_small.render('item count: {}'.format(len(items)), 1, (255, 255, 255)), (450, 25)))
    labels.append((arial_small.render('Mutation rate: {}'.format(mutation_rate), 1, (255, 255, 255)), (450, 40)))
    return labels


def main():
    """ Main program """

    ''' Adjustable Parameters '''
    population_size = 20
    mutation_rate = 0.01
    skipped_frames = 108  # recommended: values between 100 and 1000

    ''' Items '''
    WareHouse = Item()
    WareHouse.add([
		Itemloc('Watch', (49.655299, 21.159769)),
        Itemloc('Television', (50.286263, 19.104078)),
        Itemloc('Bag', (51.760229, 19.457209)),
        Itemloc('Book', (51.108314, 17.037802)),
        Itemloc('Mobile', (52.406376, 16.925167)),
        Itemloc('Laptop', (53.013790, 18.598444)),
        Itemloc('Refrigerator', (51.935619, 15.506186)),
        Itemloc('Air Conditioner', (53.428543, 14.552812)),
        Itemloc('Pendrives', (50.041187, 21.999121)),
        Itemloc('HDD', (50.049683, 19.944544)),
        Itemloc('Flash card', (53.770226, 20.490189)),
        Itemloc('Bottles', (51.245376, 22.568278))
    ])

    ''' Initialization '''
    pygame.init()
    pygame.display.set_caption('Travelling Salesman Problem')
    screen = pygame.display.set_mode((600, 700))
    stat_labels = text_labels(WareHouse.items, population_size, mutation_rate)
    ga = GeneticAlgorithm(population_size, mutation_rate, ptype=Route, args=(WareHouse.items,))
    alltime_fittest = ga.alltime_best
    alltime_fitness = 0
    refresh = True

    ''' Main loop '''
    while refresh:
        ''' Event handling '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                refresh = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        event2 = pygame.event.wait()
                        if event2.type == pygame.KEYDOWN and event2.key == pygame.K_SPACE:
                            pause = False
                        elif event2.type == pygame.QUIT:
                            pause = False
                            refresh = False

        ''' Genetic Algorithm process + statistics '''
        ga.run(reps=skipped_frames)
        current_best = ga.best()
        alltime_fittest = ga.alltime_best
        alltime_fitness = alltime_fittest.raw_fitness

        ''' Drawing part '''
        screen.fill((0, 0, 0))
        for point in map_items_onto_screen(WareHouse.items):
            pygame.draw.circle(screen, (255, 255, 255), point, 3)
        pygame.draw.aalines(screen, (100, 100, 25), True, list(map_items_onto_screen(current_best.genes)))
        pygame.draw.aalines(screen, (255, 255, 255), True, list(map_items_onto_screen(alltime_fittest.genes)))
        screen.blit(arial_small.render('Generation: {}'.format(ga.generation), 1, (255, 255, 255)), (450, 55))
        screen.blit(arial_small.render('Fitness: {:.4f}'.format(alltime_fitness), 1, (255, 255, 255)), (450, 70))
        screen.blit(arial_small.render('Current Fitness: {:.4f}'.format(current_best.raw_fitness), 1, (255, 255, 0)), (450, 85))
        for label in stat_labels:
            screen.blit(label[0], label[1])
        pygame.display.flip()

    print('Best route:', alltime_fittest)
    print('Best fitness:', alltime_fitness)


if __name__ == '__main__':
    main()
