from algorithms import zhadibnyj, vypadkovyj, genetic_alg
from input_menu import manualy, from_file, generate_all
#from experiments import conduct_experiments


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main_menu(status="задачу не задано"):
    print(f"\nГоловне меню\n"
          f"Статус задачі: {bcolors.WARNING}{status}{bcolors.ENDC}\n\n")



    print('Доступні опції:\n'
          '1. Внести дані задачі\n'
          '2. Розв\'язати задачу всіма доступними алгоритмами\n'
          '3. Провести експерименти\n'
          '4. Вивести дані задачі\n'
          '0. Завершити роботу\n')

    while True:
        state = int(input("Введіть число: "))
        if state == 0:
            print('Роботу завершено')
            break
        elif state == 1:
            input_menu()
            break
        elif state == 2:
            algorithms()
            break
        elif state == 3:
            conduct_experiments()
            break
        elif state == 4:
            # Виведення даних задачі (реалізуйте це, якщо потрібно)
            break
        else:
            print("Введіть число від 0 до 4\n")
            continue

def input_menu():
    print('\nПідменю для внесення даних задачі.\n')

    print('Доступні опції:\n'
          '1. Внести дані вручну\n'
          '2. Зчитати з файлу\n'
          '3. Згенерувати\n'
          '0. Повернутись у головне меню\n')

    while True:
        global input_data
        state = int(input("Введіть число: "))
        if state == 0:
            main_menu()
            break
        elif state == 1:
            input_data = manualy()
            break
        elif state == 2:
            input_data = from_file()

            break
        elif state == 3:
            input_data = generate_all()
            break
        else:
            print("Введіть число від 0 до 3\n")
            continue
    if input_data:
        main_menu("задачу задано")

def algorithms():
    print("\nРезультати роботи алгоритмів")
    zhad = zhadibnyj(input_data)
    vyp = vypadkovyj(input_data)
    gen = genetic_alg(input_data)
    if zhad[1] == 0:
        print("\nРезультат роботи жадібного алгоритму: обсяг продукції усіх видів не задовільняє мінімальне значення К.")
    else:
        print(f"\nРезультат роботи жадібного алгоритму: {zhad[0]}. Значення ЦФ {zhad[1]}")
    print(f"\nРезультат роботи алгоритму випадкового пошуку: {vyp[0]}. Значення ЦФ {vyp[1]}")
    print(f"\nРезультат роботи алгоритму генетичного пошуку: {gen[0]}. Значення ЦФ {gen[1]}")
if __name__ == "__main__":
    main_menu()
