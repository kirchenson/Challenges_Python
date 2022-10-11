'''Для перевозки партии грузов различной массы выделен грузовик, но его грузоподъёмность ограничена,
поэтому перевезти сразу все грузы не удастся. Грузы массой от 200 до 210 кг грузят в первую очередь,
гарантируется, что все такие грузы поместятся. На оставшееся после этого место стараются взять как можно
больше грузов. Если это можно сделать несколькими способами, выбирают тот способ, при котором самый большой
из выбранных грузов имеет наибольшую массу. Если и при этом условии возможно несколько вариантов, выбирается тот,
при котором наибольшую массу имеет второй по величине груз, и т. д. Известны количество грузов, масса каждого из них
 и грузоподъёмность грузовика. Необходимо определить количество и общую массу грузов, которые будут вывезены при
 погрузке по вышеописанным правилам.
Входные данные.
Первая строка входного файла содержит два целых числа: N — общее количество грузов и M — грузоподъёмность грузовика в кг.
 Каждая из следующих N строк содержит одно целое число — массу груза в кг.
В ответе запишите два целых числа: сначала максимально возможное количество грузов, затем их общую массу.'''

f = open('26(1).txt')
s = f.readlines()
data = s[0].split()
count = int(data[0])
memory = int(data[1])  # грузоподъемность
w = []
w210 = []  # для грузов массой  от 200 до 210
del (s[0])  # первая строка с количеством и грузоподъемностью больше не нужна

for num in s:  # распределяем числа из файла в два списка
    num = int(num)
    if 200 <= num <= 210:
        w210.append(num)
    else:
        w.append(num)

w.sort()
w210.sort(reverse=True)
res = sum(w210)  # сумма всех грузов от 200 до 210
cnt = len(w210)  # количество грузов от 200 до 210
print(w210)
if cnt > count or res > memory:
    # если кол-во грузов больше возможного или тяжелее грузоподъемности, то удаляем лишние
    while cnt > count or res > memory:
        res -= w220.pop()
        cnt -= 1

for i in range(len(w)):
    if (res < memory and memory - res >= w[i]):
        # если осталость место для других грузов, то добавляем начиная с лёгких грузов
        res += w[i]
        cnt += 1

w.sort(reverse=True)  # сортируем по убыванию список грузов, которым хватило места

for i in range(len(w)):
    for j in range(len(w)):
        # ищем максимально тяжелый груз, который может поместиться, чтобы добавить оптимальный груз
        if w[j] > w[i] and (res - w[i]) + w[j] <= memory:
            res -= w[i]
            res += w[j]

print(cnt, res) # вывод количества грузов и их общая масса
