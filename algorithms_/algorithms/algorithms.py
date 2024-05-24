import random

import numpy as np
import math

from input_menu import generate_Xj


def prybutok(a, b, c, x):
    return -a * x * x + b * x + c

def zhadibnyj(input_data):
    n, a, b, c, K, k, i = input_data
    X = generate_Xj(n)
    record = 0
    success_it = -1


    if np.sum(X) <= K:
        return X, 0

    C = []
    for i in range(n):
        C.append(prybutok(a[i], b[i], c[i], X[i]))

    result = np.round(np.sum(np.multiply(C, X)), 2)


    return X, result
def change_x(array, K):

    while True:
        riznytsa = K - np.sum(array)
        add = np.ceil(riznytsa / len(array))
        for i in range(len(array)):
            if array[i] + add > 100:
                continue
            array[i] += int(add)
        if np.sum(array) >= K:
            break

    return array


def max_result(array_of_lists):
    max_value = float('-inf')
    # Ініціалізувати змінну для зберігання списку з найбільшим першим значенням
    max_list = None


    max_index = -1  # Ініціалізація з -1, щоб вказати, що максимального значення ще не знайдено

    for i, sublist in enumerate(array_of_lists):
        if sublist[0][0] > max_value:
            max_value = sublist[0][0]
            max_list = sublist
            max_index = i

    return max_index, max_list[0]


def count_C(n,K,a,b,c):
    X = generate_Xj(n)
    if np.sum(X) <= K:
        X = change_x(X, K)

    C = []
    for i in range(n):
        C.append(prybutok(a[i], b[i], c[i], X[i]))

    result = np.round(np.sum(np.multiply(C, X)), 2)
    return [X,result]
def vypadkovyj(input_data):
    n, a, b, c, K, iterations, popul_size = input_data

    record = 0
    record_x = []
    for j in range(iterations):
        X, result = count_C(n,K,a,b,c)

        if record < result:
            record = result
            record_x = X

    return record_x, record
def genetic_alg(input_data):


    def count_parent(parent, n):
        C = [prybutok(a[i], b[i], c[i], parent[i]) for i in range(n)]
        result = np.round(np.sum(np.multiply(C, parent)), 2)
        return parent, np.sum(parent), result

    def swap_elements(parent1, parent2, start, finish):
        child1 = parent1.copy()
        child2 = parent2.copy()
        for i in range(start, finish):
            child1[i], child2[i] = child2[i], child1[i]
        return child1, child2

    def mutation(parent):
        mutation = parent.copy()
        riznytsa = (K - np.sum(parent))
        add = np.abs(riznytsa / len(parent))

        if add < 2:
            return mutation

        for i in range(len(mutation)):
            mutation[i] -= np.random.randint(1, add)
        return mutation

    def ancestor_add(population, parent1, parent2):
        parent = parent1 if parent1[2] > parent2[2] else parent2
        worst_value = max(item[1] for item in population)

        # Знаходження індексу найгіршого значення
        worst_index = [item[1] for item in population].index(worst_value)

        population[worst_index] = parent
        return population



    n, a, b, c, K, iterations, popul_size = input_data
    #генеруємо популяцію розміром k
    population = []

    for j in range(popul_size):
        res = count_C(n, K, a, b, c)
        population.append(res)


    for i in range(iterations):
        index_p1, p1 = max_result(population)
        while True:
            index_p2 = np.random.randint(0, len(population))
            if index_p1 != index_p2:
                p2 = population[index_p2][0]
                break


        start = np.random.randint(0, n - 1)
        while True:
            finish = np.random.randint(0, n - 1)
            if finish != start:
                break

        if start > finish:
            start, finish = finish, start

        child1, child2 = swap_elements(p1, p2, start, finish)
        # print(f"p1 = {child1}\n p2 = {child2}")
        parent1_mut = mutation(child1)
        parent2_mut = mutation(child2)
        # print(f"p1 = {parent1_mut}\n p2 = {parent2_mut}")
        # print(f"parent 1 = {count_parent(parent1_mut, n)}")
        # print(f"parent 2 = {count_parent(parent2_mut, n)}")

        # print(f" population = {population}")
        population = ancestor_add(population, count_parent(parent1_mut, n), count_parent(parent2_mut, n))


    # print(f" population = {population}")
    record = max(item[1] for item in population)
    record_x = [item[0] for item in population if item[1] == record]

    return record_x, record
