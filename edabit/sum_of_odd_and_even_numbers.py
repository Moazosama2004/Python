def sum_odd_and_even(lst):
    sumOdd, sumEven = 0, 0
    oddEvenList = []
    for element in lst:
        if element % 2 == 0:
            sumEven += element
        else:
            sumOdd += element
    oddEvenList.append(sumEven)
    oddEvenList.append(sumOdd)
    return oddEvenList


