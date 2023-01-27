print('Введите число для проверки на палиндром')
palNumber = int(input())


def checkPal(n):
    n = str(n)
    return n == n[::-1]


resCheck = checkPal(palNumber)
if resCheck:
    print('Число является палиндромом')
else:
    print('Число не является палиндромом')
