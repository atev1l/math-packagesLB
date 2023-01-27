print('Введите первое число')
firstNumber = str(input())
print('Введите второе число')
secondNumber = str(input())

if len(firstNumber) <= 256 and len(secondNumber) <= 256:
    print('Произведение чисел равно - ' + str(int(firstNumber) * int(secondNumber)))
else:
    print('Введите числа до 256 знаков')