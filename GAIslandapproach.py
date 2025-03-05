import random
import numpy as np

# Parameters
NUM_TASKS = 100000 # Number of tasks (simplified for demonstration)
NUM_CORES = 8   # Number of processor cores
NUM_ISLANDS = 8 # Number of islands
POPULATION_SIZE = 1250  # Population size per island
NUM_GENERATIONS = 100  # Number of generations
MIGRATION_INTERVAL = 2  # Migrate every 2 generations
MIGRATION_RATE = 1  # Number of individuals to migrate

# Generate random task execution times (for simplicity)
TASK_TIMES = [random.randint(1, 10) for _ in range(NUM_TASKS)]

# Initialize population for each island
def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        # Randomly assign tasks to cores
        chromosome = [random.randint(0, NUM_CORES - 1) for _ in range(NUM_TASKS)]
        population.append(chromosome)
    return population

# Fitness function: Calculate makespan (total execution time)
def fitness(chromosome):
    core_times = [0] * NUM_CORES
    for task, core in enumerate(chromosome):
        # Add task execution time to the assigned core
        core_times[core] += TASK_TIMES[task]
    # Makespan is the maximum core time
    return max(core_times)

# Selection: Select the best individuals
def selection(population):
    # Sort population by fitness (lower makespan is better)
    population.sort(key=lambda x: fitness(x))
    # Select top 50% of the population
    return population[:POPULATION_SIZE // 2]

# Crossover: Combine two parents to create offspring
def crossover(parent1, parent2):
    # Single-point crossover
    point = random.randint(1, NUM_TASKS - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation: Randomly change a task's core assignment
def mutate(chromosome):
    if random.random() < 0.1:  # 10% mutation rate
        task = random.randint(0, NUM_TASKS - 1)
        new_core = random.randint(0, NUM_CORES - 1)
        chromosome[task] = new_core
    return chromosome

# Migration: Exchange individuals between islands
def migrate(islands):
    for i in range(NUM_ISLANDS):
        # Select the best individuals from the current island
        migrants = selection(islands[i])[:MIGRATION_RATE]
        # Send migrants to the next island (ring topology)
        next_island = (i + 1) % NUM_ISLANDS
        islands[next_island].extend(migrants)
        # Remove the worst individuals from the next island
        islands[next_island] = selection(islands[next_island])
    return islands

# Main GA with Island Approach
def genetic_algorithm():
    # Initialize islands
    islands = [initialize_population() for _ in range(NUM_ISLANDS)]

    for generation in range(NUM_GENERATIONS):
        print(f"Generation {generation + 1}")
        for island_id, island in enumerate(islands):
            # Selection
            selected = selection(island)
            # Crossover and Mutation
            new_population = []
            while len(new_population) < POPULATION_SIZE:
                parent1, parent2 = random.choices(selected, k=2)
                child1, child2 = crossover(parent1, parent2)
                new_population.append(mutate(child1))
                new_population.append(mutate(child2))
            islands[island_id] = new_population[:POPULATION_SIZE]

            # Print best fitness in the island
            best_fitness = min([fitness(ind) for ind in islands[island_id]])
            print(f"Island {island_id + 1}: Best Fitness = {best_fitness}")

        # Migration
        if (generation + 1) % MIGRATION_INTERVAL == 0:
            print("Migrating individuals...")
            islands = migrate(islands)

    # Find the best solution across all islands
    best_solution = None
    best_fitness = float('inf')
    for island in islands:
        for individual in island:
            if fitness(individual) < best_fitness:
                best_fitness = fitness(individual)
                best_solution = individual
    print("\nBest Solution:")
    print(len(best_solution))
    print(f"Task-to-Core Mapping: {best_solution}")
    print(f"Makespan: {best_fitness}")

# Run the GA
genetic_algorithm()
