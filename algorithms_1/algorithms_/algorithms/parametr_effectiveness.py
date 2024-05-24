import numpy as np
import matplotlib.pyplot as plt
from input_menu import generator
from algorithms import genetic_alg

def profit(a, b, c, x):
    return -a * x * x + b * x + c


def total_profit(population, a, b, c):
    return np.sum(profit(a, b, c, population))


def select_parents_current(population, a, b, c):
    parent1 = population[np.argmax([total_profit(individual, a, b, c) for individual in population])]
    parent2 = population[np.random.randint(0, len(population))]
    return parent1, parent2


def select_parents_tournament(population, a, b, c):
    parent1 = population[np.random.randint(0, len(population))]
    parent2 = population[np.random.randint(0, len(population))]
    return parent1, parent2


def crossover(parent1, parent2, start, finish):
    child1, child2 = parent1.copy(), parent2.copy()
    temp1, temp2 = parent1[start:finish].copy(), parent2[start:finish].copy()
    child1[start:finish], child2[start:finish] = temp2, temp1
    return child1, child2

# Функція мутації
def mutate(individual):
    mutation_rate = 0.1  
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = np.random.randint(10, 101)  
    return individual

# Функція проведення експерименту
def experiment(population_size, generations, a, b, c, selection_method):
    population = np.random.randint(10, 101, size=(population_size, len(a)))  # Початкова популяція
    best_profit_per_generation = []  #найкращ прибуток на кожному поколінні

    for _ in range(generations):
        record = genetic_alg([n, a, b, c, K, iterations, population_size],selection_method)
        best_profit_per_generation.append(record[1])

    return best_profit_per_generation

# Параметри експерименту
n = 30  
population_size = 50  
generations = 100
iterations = 50
K = 289

a = np.random.uniform(0.005, 0.02, n)
b = np.random.uniform(0.02, 0.04, n)
c = np.random.randint(150, 301, n)


current_selection_results = experiment(population_size, generations, a, b, c, 0)


tournament_selection_results = experiment(population_size, generations, a, b, c, 1)


plt.plot(current_selection_results, label='Поточний вибір батьків')
plt.plot(tournament_selection_results, label='Турнірний вибір батьків')
plt.xlabel('Покоління')
plt.ylabel('Найкращий прибуток')
plt.title('Вплив методу вибору батьків на ефективність генетичного алгоритму')
plt.legend()
plt.grid(True)
plt.savefig('param_gen')
plt.show()
