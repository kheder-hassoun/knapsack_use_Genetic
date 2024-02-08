
# kheder hassoun knap sack problem 
import random

# Define item and knapsack parameters
items = [ 
  
    (5, 5),
     (0, 5),
    (11, 2),
    (4, 10),
    (50, 5),
     (10, 5),
    (75, 2),
     (10, 5),
    (75, 2),
    (50, 18),
    (30, 25),
    (1, 5)] # List of tuples (value, weight)

max_weight = 50 # Maximum weight capacity of the knapsack

# Genetic Algorithm parameters
population_size = 50
number_of_generations = 100
crossover_rate = 0.7
mutation_rate = 0.01

# Initialize population
# creat a list of lists 😁 in each list 1 means that we takee the item ✔ ,  0 we dont  ..
population = [[random.randint(0, 1) for _ in range(len(items))] for _ in range(population_size)]

# Fitness function
def fitness(chromosome):
    total_value, total_weight = 0, 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_value += items[i][0]
            total_weight += items[i][1]
    if total_weight > max_weight:
        return 0 # Penalize if over max weight
    return total_value

# Selection function

def select(population):
    new_pop = []# the new slected puploatin ⚠ must be the same old popluation length 😁
    # ارندم من هيك ما في 😁❤
    while len(new_pop) < len(population):
        num_participants = random.randint(2, len(population))
        participants = random.sample(population, num_participants)
        temp = max(participants, key=fitness)
        new_pop.append(temp)

    return new_pop
# Crossover function
def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        crossover_postion = int(random.uniform(1, len(parent1)))# or we can use a const value but this will make a more defferance (using ranmdom)  🙄
        new_pretty_baby1 = parent1[:crossover_postion] + parent2[crossover_postion:]
        new_pretty_baby2 = parent2[:crossover_postion] + parent1[crossover_postion:]
     
        return new_pretty_baby1, new_pretty_baby2
    else:
        return parent1, parent2


# Mutation function

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # swap 😁🙄
    return chromosome


# Genetic Algorithm
for generation in range(number_of_generations):
    print(' genatation    ', generation  , "✔")
    # Evaluate fitness
    fitness_values = [fitness(chromosome) for chromosome in population]

    # Selection
    parents = select(population)

    # Crossover
    offspring = []
    for i in range(0, len(parents), 2):
        child1, child2 = crossover(parents[i], parents[i+1])
        offspring.append(child1)
        offspring.append(child2)

    # Mutation
    for child in offspring:
        mutate(child)

    # Create new population
    population = offspring
    print(' genatation    ', '\033[94m' +str(generation)  , "✔  " ,str(max(population, key=fitness)) )
# Find the best solution
# '\033[94m'  this code is to changge the terminal color 😁
best_chromosome = max(population, key=fitness)
print('\n'+ '\033[91m'+'the origanal itemes :  '+'\033[92m', items)
print( '\n' '\033[91m'+'Best Solution: ' +'\033[93m', best_chromosome)
print()
k = input(" press any f key to continue")