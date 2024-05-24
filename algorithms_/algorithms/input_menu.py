import csv

import numpy as np
import os

# a = [0.12, 0.0055, 0.003, 0.075]
# b = [0.021, 0.036, 0.028, 0.031]
# c = [300,260,299,201]
# K = 230
# k = 3

a_min = 0.005; a_max = 0.02
b_min = 0.02; b_max = 0.04
c_min = 150; c_max = 300



def get_csv_files(directory):
    csv_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            csv_files.append(filename)
    return csv_files


def input_positive_integer(prompt, from_to = 0):
    while True:
        try:
            value = int(input(prompt))
            if from_to == 0:
                if value > 0:
                    return value
                else:
                    print("Число повинно бути більше нуля.")
            else:
                if from_to[0]<= value <= from_to[1]:
                    return value
                else:
                    print(f"Число повинно бути в межах ({from_to[0]}; {from_to[1]}).")
        except ValueError:
            print("Введіть ціле число")


def input_array(prompt, n, min_value, max_value):
    while True:
        try:
            input_elements = input(prompt).split()
            if len(input_elements) != n:
                print(f"Введіть рівно {n} значень.")
                continue
            array = [float(element) for element in input_elements]
            if all(min_value <= element <= max_value for element in array):
                return array
            else:
                print(f"Всі значення повинні бути в діапазоні ({min_value}; {max_value}).")
        except ValueError:
            print("Всі елементи повинні бути числами.")


def generate_Xj(n):
    Xj = np.random.randint(10, 100, size=(n))
    return Xj

def prybutok(a, b, c, x):
    return -a * x * x + b * x + c

# x = [[98, 53, 82, 31],
#      [84, 58, 73, 41],
#      [76, 60, 69, 54]]


def manualy():
    n = input_positive_integer("Введіть кількість виробів(n): ")
    a = input_array(f"Введіть значення параметру вартості (а) для кожного виду через пробіл ({n} значень у діапазоні ({a_min}; {a_max})): ", n, a_min, a_max)
    b = input_array(f"Введіть значення параметру вартості (b) для кожного виду через пробіл ({n} значень у діапазоні ({b_min}; {b_max})): ", n, b_min, b_max)
    c = input_array(f"Введіть значення параметру вартості (c) для кожного виду через пробіл ({n} значень у діапазоні ({c_min}; {c_max})): ", n, c_min, c_max)
    K = input_positive_integer(f"Введіть мінімальний обсяг випуску продукції за місяць (у діапазоні ({10*n}; {100*n}, K): ", [10*n,100*n])
    k = input_positive_integer("Введіть кількість ітерацій(k): ")
    i = input_positive_integer("Введіть кількість особин популяції (i): ")


    print("Нові дані збережено успішно!\n")
    return n,a,b,c,K,k
def from_file():
    project_directory = "D:/semestr_6/kursova/algorithms_/algorithms"
    csv_files = get_csv_files(project_directory)
    print("CSV файли у директорії:")
    for i in range(len(csv_files)):
        print(f"{i} - {csv_files[i]}")

    while(True):
        try:
            path = int(input("Введіть номер файлу який треба відкрити: "))
            file = csv_files[path]
            break
        except IndexError:
            print("Не існує такого файлу. Введіть правильний номер файлу.\n")
        except FileNotFoundError:
            print("Файл не знайдено. Спробуйте ще раз.\n")
        except ValueError:
            print("Введіть коректний номер файлу.\n")


    with open(file) as f:
        n = int(f.readline())
        a = list(map(float, f.readline().split()))
        b = list(map(float, f.readline().split()))
        c = list(map(float, f.readline().split()))
        K = float(f.readline())
        k = int(f.readline())
        i = int(f.readline())


        print("Дані зчитано успішно!\n")

    return n, a, b, c, K, k,i

def generate_all():
    n = input_positive_integer("\nВведіть кількість виробів(n): ")
    print(f"\n\nЗначення параметрів вартості а,b,c згенеровані випадковим чином в межах умови задачі.")
    a = np.random.uniform(a_min, a_max, n)
    b = np.random.uniform(b_min, b_max, n)
    c = np.random.uniform(c_min, c_max, n)
    insert = input(f"\n\nМінімальний обсяг випуску продукції (К) за місяць буде згенеровано у діапазоні ({10*n}; {100*n})\n"
                   f"Можна змінити межі межі за потреби. Змінити межі (+/-)?")
    if insert == "+":
        minimum = input("Значення нижньої межі:")
        maximum = input("Значення верхньої межі:")
        K = np.random.randint(minimum, maximum)
    else:
        K = np.random.randint(10 * n, 100 * n)

    insert = input(
        f"\n\nКількість ітерацій (k) буде згенеровано у діапазоні (1;20)\n"
        f"Можна змінити межі межі за потреби. Змінити межі (+/-)?")
    if insert == "+":
        minimum = input("Значення нижньої межі:")
        maximum = input("Значення верхньої межі:")
        k = np.random.randint(minimum, maximum)
    else:
        k = np.random.randint(1, 20)

    insert = input(
        f"\n\nКількість особин популяції (i) буде згенеровано у діапазоні (1;20)\n"
        f"Можна змінити межі межі за потреби. Змінити межі (+/-)?")
    if insert == "+":
        minimum = input("Значення нижньої межі:")
        maximum = input("Значення верхньої межі:")
        i = np.random.randint(minimum, maximum)
    else:
        i = np.random.randint(1, 20)

    print("\nНові дані збережено успішно!\n")
    return n, a, b, c, K, k, i





def generator(n):

    a = np.random.uniform(a_min, a_max, n)
    b = np.random.uniform(b_min, b_max, n)
    c = np.random.uniform(c_min, c_max, n)
    iterations = 4
    K = np.random.randint(10 * n, 100 * n)
    pop_s = np.random.randint(2, 20)



    return n, a, b, c, K, iterations, pop_s








