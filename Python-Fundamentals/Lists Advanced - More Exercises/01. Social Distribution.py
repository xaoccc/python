population = [int(i) for i in input().split(", ")]
min_wealth = int(input())

if sum(population) < min_wealth * len(population):
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        wealthiest_index = population.index(max(population))
        if population[i] < min_wealth:
            population[wealthiest_index] -= (min_wealth - population[i])
            population[i] = min_wealth
    print(population)
