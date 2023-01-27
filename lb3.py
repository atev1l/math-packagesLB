def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


print('Введите число')
number = str(input())
newNumber = '1' + number + '1'

resPrime = IsPrime(int(newNumber))
if resPrime:
    print('Число ' + newNumber + ' является простым')
else:
    print('Число ' + newNumber + ' не является простым')