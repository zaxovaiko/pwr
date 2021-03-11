import ga

if __name__ == '__main__':
    ga.initiate_population()
    ga.fitness_score()

    while True:
        ga.tournament_selection()
        ga.uniform_crossover()
        ga.fitness_score()
