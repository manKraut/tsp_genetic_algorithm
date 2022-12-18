import random
import math
import matplotlib.pyplot as plt


# get cities info
def get_city():
    cities = []
    f = open("cities_coordinates.txt")
    for i in f.readlines():
        node_city_val = i.split()
        cities.append(
            [node_city_val[0], float(node_city_val[1]), float(node_city_val[2])]
        )

    return cities


# calculating distance of the cities
def calc_distance(cities):
    total_sum = 0
    for i in range(len(cities) - 1):
        city_a = cities[i]
        city_b = cities[i + 1]

        d = math.sqrt(
            math.pow(city_b[1] - city_a[1], 2) + math.pow(city_b[2] - city_a[2], 2)
        )

        total_sum += d

    city_a = cities[0]
    city_b = cities[-1]
    d = math.sqrt(math.pow(city_b[1] - city_a[1], 2) + math.pow(city_b[2] - city_a[2], 2))

    total_sum += d

    return total_sum


# selecting the population
def select_population(cities, size):
    population = []

    for i in range(size):
        c = cities.copy()
        random.shuffle(c)
        distance = calc_distance(c)
        population.append([distance, c])
    fitest = sorted(population)[0]

    return population, fitest


# the genetic algorithm
def genetic_algorithm(
    population,
    len_of_cities,
    tournament_selection_size,
    mutation_rate,
    crossover_rate,
    target,
):
    gen_number = 0
    for i in range(200):
        # selecting two of the best options we have (elitism)
        new_population = [sorted(population)[0], sorted(population)[1]]
        for i in range(int((len(population) - 2) / 2)):
            # crossover
            random_number = random.random()
            if random_number < crossover_rate:
                parent_chromosome1 = sorted(
                    random.choices(population, k=tournament_selection_size)
                )[0]

                parent_chromosome2 = sorted(
                    random.choices(population, k=tournament_selection_size)
                )[0]

                point = random.randint(0, len_of_cities - 1)

                child_chromosome1 = parent_chromosome1[1][0:point]
                for j in parent_chromosome2[1]:
                    if not (j in child_chromosome1):
                        child_chromosome1.append(j)

                child_chromosome2 = parent_chromosome2[1][0:point]
                for j in parent_chromosome1[1]:
                    if not (j in child_chromosome2):
                        child_chromosome2.append(j)

            # If crossover not happen
            else:
                child_chromosome1 = random.choices(population)[0][1]
                child_chromosome2 = random.choices(population)[0][1]

            # MUTATION
            if random.random() < mutation_rate:
                point1 = random.randint(0, len_of_cities - 1)
                point2 = random.randint(0, len_of_cities - 1)
                child_chromosome1[point1], child_chromosome1[point2] = (
                    child_chromosome1[point2],
                    child_chromosome1[point1],
                )

                point1 = random.randint(0, len_of_cities - 1)
                point2 = random.randint(0, len_of_cities - 1)
                child_chromosome2[point1], child_chromosome2[point2] = (
                    child_chromosome2[point2],
                    child_chromosome2[point1],
                )

            new_population.append([calc_distance(child_chromosome1), child_chromosome1])
            new_population.append([calc_distance(child_chromosome2), child_chromosome2])

        population = new_population

        gen_number += 1

        if gen_number % 10 == 0:
            print(gen_number, sorted(population)[0][0])

        if sorted(population)[0][0] < target:
            break

    answer = sorted(population)[0]

    return answer, gen_number


# draw cities and answer map
def draw_map(city, answer):
    for j in city:
        plt.plot(j[1], j[2], "ro")
        plt.annotate(j[0], (j[1], j[2]))

    for i in range(len(answer[1])):
        try:
            first = answer[1][i]
            secend = answer[1][i + 1]

            plt.plot([first[1], secend[1]], [first[2], secend[2]], "gray")
        except:
            continue

    first = answer[1][0]
    secend = answer[1][-1]
    plt.plot([first[1], secend[1]], [first[2], secend[2]], "gray")

    plt.show()


def main():
    # initial values
    population_size = 2000
    tournament_selection_size = 4
    mutation_rate = 0.1
    crossover_rate = 0.9
    target = 450.0

    cities = get_city()
    first_population, first_fitest = select_population(cities, population_size)
    answer, gen_number = genetic_algorithm(
        first_population,
        len(cities),
        tournament_selection_size,
        mutation_rate,
        crossover_rate,
        target,
    )

    print("\n----------------------------------------------------------------")
    print("Generation: " + str(gen_number))
    print("Fittest chromosome distance before training: " + str(first_fitest[0]))
    print("Fittest chromosome distance after training: " + str(answer[0]))
    print("Target distance: " + str(target))
    print("----------------------------------------------------------------\n")

    draw_map(cities, answer)


if __name__ == '__main__':
    main()
