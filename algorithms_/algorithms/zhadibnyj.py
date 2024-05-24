import numpy as np

a = [0.012, 0.0055, 0.003, 0.075]
b = [0.021, 0.036, 0.028, 0.031]
c = [300,260,299,201]
K = 230
k = 3


def prybutok(a, b, c, x):
    print(-a * x * x + b * x + c)
    return -a * x * x + b * x + c


x = [[98, 53, 82, 31],
     [84, 58, 73, 41],
     [76, 60, 69, 54]]

record = 0
for j in range(k):
    print('\nІтерація', j+1, ':')
    print('xj= ', x[j])

    if (np.sum(x[j]) <= K):
        print('Перевірка К НЕ пройдена')
        continue

    C = []
    for i in range(4):
        C.append(prybutok(a[i], b[i], c[i], x[j][i]))


    result = np.round(np.sum(np.multiply(C, x[j])),2)

    if j == 0:
        record = result
        success_it = j
    else:
        if record<result:
            record = result
            success_it = j
    print('Обчислений прибуток = ', result)
    print('Рекордний прибуток = ', record)

print('\nОтже, рекордний прибуток = ', record)
print('При значеннях xj= ', x[success_it])


