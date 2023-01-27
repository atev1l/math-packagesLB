print('Введите число')
number = int(input())

def isFactorial(n):
    i, f = 1, 1
    while f < n:
        i += 1
        f *= i
    if (n == f):
        return i
    else:
        return 'не является факториалом никокого числа'


print(isFactorial(number))