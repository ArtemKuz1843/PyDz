# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем
# пользователь вводит сами элементы множеств.

n = int(input('Введите раазмер первого набора n: '))
kit1 = []
for i in range(n):
    i = int(input('Введите число в набор n: '))
    kit1.append(i)
print(kit1)
kit1 = set(kit1)

m = int(input('Введите раазмер второго набора m: '))
kit2 = []
for i in range(m):
    i = int(input('Введите число в набор m: '))
    kit2.append(i)
print(kit2)
kit2 = set(kit2)

kit3 = kit1.intersection(kit2)
kit3 = sorted(list(kit3))
print(f'Пересечение наборов и сортировка: {kit3}')