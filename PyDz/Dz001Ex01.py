# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input('Введите трёхзначное число: '))

mum1 = num % 10
mum2 = num // 10 % 10
mum3 = num // 100 % 10

summa = mum3 + mum2 + mum1

print(f'Число соответственно, 1е - {mum3}, 2е - {mum2}, 3е - {mum1}')
print(f'Сумма чисел: {summa}')