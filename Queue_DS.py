stock_price_queue = []

stock_price_queue.insert(0, 100.01)
stock_price_queue.insert(0, 123.01)
stock_price_queue.insert(0, 135.01)
stock_price_queue.insert(0, 140.01)

print(stock_price_queue)

stock_price_queue.pop()
stock_price_queue.pop()

print(stock_price_queue)

from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(6)
q.appendleft(7)
q.appendleft(8)

q.pop()
q.pop()

print(q)

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.appendleft(val)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[-1]
    


def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()

produce_binary_numbers(10)
    
pq = Queue()

pq.enqueue({
    'company': "tata motors",
    'timestamp': "11.01 AM",
    'price': 131.30,
})
pq.enqueue({
    'company': "tata motors",
    'timestamp': "11.02 AM",
    'price': 131.50,
})
pq.enqueue({
    'company': "tata motors",
    'timestamp': "11.03 AM",
    'price': 131.60,
})
pq.enqueue({
    'company': "tata motors",
    'timestamp': "11.04 AM",
    'price': 131.20,
})

print(pq.queue)

print(pq.size())

print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())

# import time
# import threading

# orders = ['pizza','samosa','pasta','biryani','burger']

# food_order_queue = Queue()

# def place_order(orders):
#     for i in orders:
#         time.sleep(0.5)
#         food_order_queue.enqueue(i)
#         print('Order Placed : ' ,i )

# def serve_order():
#     while True:
#         time.sleep(2)
#         order = food_order_queue.dequeue()
#         print('Order Served : ' ,order)

# t = time.time()

# t1 =threading.Thread(target=place_order, args=(orders,))
# t2 =threading.Thread(target=serve_order)

# t1.start()
# time.sleep(1)
# t2.start()

# t1.join()
# t2.join()
