print('Введите количество красных бактерий')
countRedB = int(input())

print('Введите количество зеленых бактерий')
countGreenB = int(input())

print('Введите количество времени')
countTime = int(input())

for i in range(countTime):
    countGreenB = (countGreenB * 2) + countRedB
print(countRedB)
print(countGreenB)