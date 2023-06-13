# O(n2)
def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

elements = [21,38,29,17,4,25,11,32,9]

shell_sort(elements)
print(elements)

tests = [
    [11,9,29,7,2,15,28],
    [3, 7, 9, 11],
    [25, 22, 21, 10],
    [29, 15, 28],
    [],
    [6]
]

for elements in tests:
    shell_sort(elements)
    print(f'sorted array: {elements}')


elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]

shell_sort(elements)
print(list(set(elements)))

