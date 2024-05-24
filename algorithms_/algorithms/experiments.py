import matplotlib.pyplot as plt
import numpy as np
import time
from algorithms import zhadibnyj, genetic_alg, vypadkovyj
from input_menu import generator


def measure_time(algorithm, *args):
    start_time = time.time()
    algorithm([*args])
    end_time = time.time()
    return end_time - start_time

def run_experiments(input_data):


    greedy_time = measure_time(zhadibnyj, *input_data)
    random_search_time = measure_time(vypadkovyj, *input_data)
    genetic_time = measure_time(genetic_alg, *input_data)



    return greedy_time, random_search_time, genetic_time

def plot_results(n_values, greedy_times, random_search_times, genetic_times):
    plt.plot(n_values, greedy_times, label='Жадібний алгоритм')
    plt.plot(n_values, random_search_times, label='Алгоритм випадкового пошуку')
    plt.plot(n_values, genetic_times, label='Генетичний алгоритм')
    plt.xlabel('Кількість виробів (n)')
    plt.ylabel('Час (секунди)')
    plt.title('Вплив розмірності задачі на час роботи алгоритмів')
    plt.legend()
    plt.show()

def conduct_experiments():

    start_n = 10
    end_n = 100
    Nj = np.arange(start_n, end_n+10, 10)
    greedy_times = []
    random_search_times = []
    genetic_times = []
    for n in Nj:
        n_greedy_times = []
        n_random_search_times = []
        n_genetic_times = []
        for i in range(20):
            input_data = generator(n)
            a, b, c = run_experiments(input_data)
            n_greedy_times.append(a)
            n_random_search_times.append(b)
            n_genetic_times.append(c)
        greedy_times.append(np.mean(n_greedy_times))
        random_search_times.append(np.mean(n_random_search_times))
        genetic_times.append(np.mean(n_genetic_times))

    plot_results(Nj, greedy_times, random_search_times, genetic_times)




conduct_experiments()

