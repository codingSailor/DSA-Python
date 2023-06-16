# Time complexity O(1) - Search/Access/Insert/Delete

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val

    # OR

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # self.arr[h] = value

        #handling collision by separate chaining

        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0]==key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))


    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]
    
    # OR

    def __getitem__(self, key):
        h = self.get_hash(key)
        # return self.arr[h]

        for element in self.arr[h]:
            if element[0] == key:
                return[1]
    
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        # self.arr[h] = None

        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]



    
    

t = HashTable()
print(t.get_hash('march 6'))
# t.add('march 6', 130)
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
# print(t.get['march 6'])
print(t['march 6'])
print(t.arr)
t["march 6"] = 11
print(t.arr)


#Exercises of python dictionary

arr = []

with open("nyc_weather.csv", 'r') as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print('Invalid temp, ignore the row')

print(arr)

print(sum(arr[0:7])/7)
print(max(arr[0:10]))

temp_dict = {}

with open("nyc_weather.csv") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            temp_dict[tokens[0]] = temperature
        except:
            print('Invalid temp, ignore the row')

print(temp_dict)

print(temp_dict['Jan 9'])
print(temp_dict['Jan 4'])


word_count = {}
with open('poem.txt', 'r') as f:
    for line in f:
        tokens = line.split(' ')
        # print(tokens)
        for token in tokens:
            token = token.replace('\n','')
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

print(word_count)
