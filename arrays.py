list = [2200,2350,2600,2130,2190]

#1 Ques

diff = list[1]-list[0]
print(diff)

#2 Ques

total3 = list[0]+list[1]+list[2]
print(total3)

#3 Ques

for i in range(len(list)):
    if 2000 == list[i]:
        print(i)

#OR

print(2000 in list)

#4 Ques

list.append(1980)

print(list)

#5 ques

list[3] = list[3]-200

print(list)

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('black panther')

print(heros)

heros.remove('black panther')

heros.insert(3,'black panther')

print(heros)

heros[1:3]=['doctor strange']

print(heros)

# print(dir(heros))

heros.sort()

print(heros)

n = int(input('Enter a number :'))

list = [x for x in range(n) if x%2 != 0]

print(list)