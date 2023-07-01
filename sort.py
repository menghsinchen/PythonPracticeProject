def BubbleSort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

numbers = [1,2,5,8,3]
print("Before Sorting:", numbers)
BubbleSort(numbers)
print("After Sorting:", numbers)