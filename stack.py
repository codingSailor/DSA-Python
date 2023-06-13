#LIFO


# s = []

# s.append('1')
# s.append('2')
# s.append('3')
# s.append('4')
# s.append('5')

# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(stack.pop())

print(stack)

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    
    def view(self):
        return self.container
    

s = Stack()

s.push(5)

print(s.peek())

s.push(6)
s.push(7)
s.push(8)
s.push(9)
print(s.peek())
s.pop()
s.pop()
s.pop()
print(s.size())
print(s.view())
s.pop()
s.pop()

#Exercise

str = "We will conquere COVID-19"

for char in str:
    s.push(char)

reverse_string = ''
for i in range(len(str)):
    reverse_string += s.pop()

print(str)
print(reverse_string)


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0
    
print(is_balanced("({a+b})}"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))