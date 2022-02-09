array = [2, 4, 1, -100, 3, 1000, 1.5, 2, 2, 2, 2.5, 2, 3, 500]
print(f'Unsorted list: {array}')

for i in range(1, len(array)):
    for j in range(len(array)):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

print(f'Sorted list: {array}')
