#Time Complexity : O(n^2)

def bubble_sort(elements):

    size = len(elements)

    for i in range(size-1):
        swapped = False         #O(n)
        for j in range(size-1):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break


# elements = [5,9,2,1,67,34,88,34]
elements = [x for x in range(10)]

bubble_sort(elements)
print(elements)


# Exercise


def bubble_sort(elements, key):    

    size = len(elements)

    for i in range(size-1):
        swapped = False         #O(n)
        for j in range(size-1):
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break


# elements = [5,9,2,1,67,34,88,34]
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

bubble_sort(elements,'transaction_amount')
print('By amount',elements)
bubble_sort(elements,'name')
print('By name',elements)

