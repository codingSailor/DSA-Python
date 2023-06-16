# Time complexity : O(nlogn)


def merge_sort(arr):

    if len(arr) <= 1:
        return 
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    # left = merge_sort(left)
    # right = merge_sort(right)

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)
    # return merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b, arr):
    # sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            # sorted_list.append(a[i])
            arr[k] = a[i]
            i+=1
        else:
            # sorted_list.append(b[j])
            arr[k] = b[j]
            j+=1
        k+=1
    while i < len_a:
        # sorted_list.append(a[i])
        arr[k] = a[i]
        i+=1
        k+=1
    while j < len_b:
        # sorted_list.append(b[j])
        arr[k] = b[j]
        j+=1
        k+=1

    # return sorted_list

a = [5,8,12,56]
b = [7,9,45,51]

arr = [7,9,45,51,5,8,12,56]

# print(merge_two_sorted_lists(a,b))

# print(merge_sort(arr))

# ------ #

tests = [
    [11,9,29,7,2,15,28],
    [3, 7, 9, 11],
    [25, 22, 21, 10],
    [29, 15, 28],
    [],
    [6]
]

# for elements in tests:
#     merge_sort(elements)
#     print(f'sorted array: {elements}')

# merge_sort(arr)

# print(arr)


# Exercise


def ex_merge_sort(arr, key, desc=False):

    if len(arr) <= 1:
        return 
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    # left = merge_sort(left)
    # right = merge_sort(right)

    ex_merge_sort(left, key, desc)
    ex_merge_sort(right, key, desc)

    ex_merge_two_sorted_lists(left, right, arr, key, desc)
    # return merge_two_sorted_lists(left, right, arr)

def ex_merge_two_sorted_lists(a,b, arr, key , desc):
    # sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if desc:
            if a[i][key] >= b[j][key]:
                # sorted_list.append(a[i])
                arr[k] = a[i]
                i+=1
            else:
                # sorted_list.append(b[j])
                arr[k] = b[j]
                j+=1
            k+=1
        else: 
            if a[i][key] <= b[j][key]:
                # sorted_list.append(a[i])
                arr[k] = a[i]
                i+=1
            else:
                # sorted_list.append(b[j])
                arr[k] = b[j]
                j+=1
            k+=1
            
    while i < len_a:
        # sorted_list.append(a[i])
        arr[k] = a[i]
        i+=1
        k+=1
    while j < len_b:
        # sorted_list.append(b[j])
        arr[k] = b[j]
        j+=1
        k+=1


arr = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

ex_merge_sort(arr, 'name', True)
ex_merge_sort(arr, 'name')
print(arr)