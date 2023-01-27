def maxProduct(arrayList):
    if len(arrayList) < 3:
        raise Exception('В массиве меньше трех чисел')

    highest = max(arrayList[0], arrayList[1])
    lowest = min(arrayList[0], arrayList[1])
    highestProductOf2 = arrayList[0] * arrayList[1]
    lowestProductOf2 = arrayList[0] * arrayList[1]

    highestProductOfThree = arrayList[0] * arrayList[1] * arrayList[2]

    for current in arrayList[2:]:
        highestProductOfThree = max(highestProductOfThree, current * highestProductOf2, current * lowestProductOf2)
        highestProductOf2 = max(highestProductOf2, current * highest, current * lowest)
        lowestProductOf2 = min(lowestProductOf2, current * highest, current * lowest)
        highest = max(highest, current)
        lowest = min(lowest, current)

    return highestProductOfThree


print(maxProduct([-4, -66, 4, 66, 2, 4]))