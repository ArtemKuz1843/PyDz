# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех
# арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4
num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))

def sumRecurs(numb1, numb2):
    if numb2 == 0:
        return numb1
    return 1 + sumRecurs(numb1, numb2 - 1)

print(f"Сумма чисел: {sumRecurs(num1, num2)}")