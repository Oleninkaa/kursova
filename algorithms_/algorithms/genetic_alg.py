import numpy as np
import math
n=4
a = [0.012, 0.0055, 0.003, 0.075]
b = [0.021, 0.036, 0.028, 0.031]
c = [300,260,299,201]
K = 230
k = 3


def prybutok(a, b, c, x):
    return -a * x * x + b * x + c


X_ = [[20, 89, 75],
     [31, 67, 73],
     [97, 59, 25],
     [90, 91, 23]]

X = np.transpose(X_)


def count_parent(parent, n):
    C = []
    for i in range(n):
        C.append(prybutok(a[i], b[i], c[i], parent[i]))

    result = np.round(np.sum(np.multiply(C, parent)), 2)
    return parent, np.sum(parent), result


def ancestors(parent1, parent2, start, finish):

    temp_p1 = parent1[start:finish]
    temp_p2 = parent2[start:finish]

    parent1[start:finish] = temp_p2
    parent2[start:finish] = temp_p1

    if (np.sum(parent1) <= K):
        parent1 = change_x(parent1)

    if (np.sum(parent2) <= K):
        parent2 = change_x(parent2)

    return parent1, parent2


def mutation(parent):
    riznytsa = (K - np.sum(parent))
    add = np.abs(riznytsa / len(parent))

    if add <2:
        return parent

    for i in range(len(parent)):
        parent[i] -= np.random.randint(1, add)
    return parent


def change_x(array):
    riznytsa = (K-np.sum(array))
    add = math.ceil(riznytsa/len(array))

    for i in range(len(array)):
        array[i] += add
    return array


def ancestor_add(population, parent1, parent2):

    if parent1[2] > parent2[2]:
        parent = parent1
    else:
        parent = parent2

    min_index = min(range(len(population)), key=lambda i: population[i][2])
    if population[min_index][2] < parent[2]:
        population[min_index] = parent
    return population





    print(f"record = {record}\n minimum = {minimum}")



record = 0
success_it = -1
values = []

for j in range(k):
    if (np.sum(X[j]) <= K):
        X[j] = change_x(X[j])

    C = []
    for i in range(n):
        C.append(prybutok(a[i], b[i], c[i], X[j][i]))

    result = np.round(np.sum(np.multiply(C, X[j])), 2)
    values.append(result)

    if j == 0:
        record = result
        success_it = j
    else:
        if record < result:
            record = result
            success_it = j
    print("\n\nkst = ", np.sum(X[j]))
    print('Обчислений прибуток = ', result)
    print('Рекордний прибуток = ', record)

print(f"values = {values}\n\n")
print(f" Найкраще значення: {X[success_it]}. Значення ЦФ {record}")
population = []
for i in range(len(values)):
    population.append([X[i].tolist(), np.sum(X[i]), values[i]])
print(f"population = {population}")


print("\n--------------------------------------------------\n")
parent1_index = success_it
while True:
    parent2_index = np.random.randint(0, k)
    if parent2_index != parent1_index:
        break
print("Індекс першого батька: ", parent1_index)
print("Індекс другого батька: ", parent2_index)

tochka_width = np.random.randint(1, n - 1)
start = np.random.randint(0, n - 1)  # починаючи з
finish = (start + tochka_width) % n  # перед
print("Ширина: ", tochka_width)
print(f"Точки схрещування: {start}, {finish}")

parent1= []
parent2 = []
for j in range(n):
    parent1.append(X[parent1_index][j])
    parent2.append(X[parent2_index][j])


print(f"\nParent 1: {count_parent(parent1, n)}")
print(f"Parent 2: {count_parent(parent2, n)}\n")


# start = 1
# finish = 3



parent1_anc, parent2_anc = ancestors(parent1, parent2, start, finish)
print(f"-----------Нащадки-----------")
print(f"\nParent 1: {count_parent(parent1_anc, n)}")
print(f"Parent 2: {count_parent(parent2_anc, n)}\n")

parent1_mut = mutation(parent1)
parent2_mut = mutation(parent2)
print(f"-----------Мутація-----------")
print(f"\nParent 1: {count_parent(parent1_mut, n)}")
print(f"Parent 2: {count_parent(parent2_mut, n)}\n")

print(f"population = {population}")
population = ancestor_add(population, count_parent(parent1_mut, n), count_parent(parent2_mut, n))
print(f"population = {population}")


#
# print('\nОтже, рекордний прибуток = ', record)
# print('При значеннях xj= ', X[success_it])


def prybutok(a, b, c, x):
    return -a * x * x + b * x + c








