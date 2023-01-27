import math

print('Введите число')
number = str(input())
try:
    if 0 <= int(number) <= 1000:
        print('Количество нулей - ' + str(str(math.factorial(int(number))).count('0')))
except Exception as err:
    print('Введите число от 0 до 1000')