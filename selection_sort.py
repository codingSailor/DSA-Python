# O(n2)

def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i
        for j in range(min_index+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i] , arr[min_index] = arr[min_index], arr[i]

    pass

# def find_min_element(arr):
#     min = 10000000
#     for i in range(len(arr)):
#         if arr


elements = [21,38,29,17,4,25,11,32,9]

selection_sort(elements)
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
    selection_sort(elements)
    print(f'sorted array: {elements}')


# Exercise

def ex_selection_sort(arr, keys):
    size = len(arr)

    for k in keys[-1::-1]:
        for i in range(size):
            min_index = i
            for j in range(min_index+1, size):
                if arr[j][k] < arr[min_index][k]:
                    min_index = j
            if i != min_index:
                arr[i] , arr[min_index] = arr[min_index], arr[i]

    pass


elements = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

ex_selection_sort(elements, ['First Name', 'Last Name'])
print(f'sorted array: ',elements, sep='\n')