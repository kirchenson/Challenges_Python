'''Пусть M(N) — произведение 5 наименьших различных натуральных делителей натурального числа N, не считая единицы.
 Если у числа N меньше 5 таких делителей, то M(N) считается равным нулю.
Найдите 5 наименьших натуральных чисел, превышающих 500 000 000, для которых 0 < M(N) < N.
 В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.'''

def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d

for x in range(500_000_001, 500_000_100):
    if len(div(x)) >= 5:
        d = sorted(div(x))
        p = 1
        for i in range(5):
            p *= d[i]
        if p < x:
            print(p)
