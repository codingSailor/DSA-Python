class Node:
    def __init__(self,data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        itr = self.head
        node = Node(data, self.head, None)
        itr.prev = node
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '<-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        
        if index==0:
            self.head = self.head.next
            self.head.prev = None

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                itr.next.next.prev = itr
                break
            itr = itr.next
            count += 1

    def insert_at(self, index,data):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break

            itr = itr.next
            count +=1
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        itr = self.head
        found = 0
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                found = 1
                break

            itr = itr.next

        if found == 0:
            raise Exception('Data not found')
    
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        
        itr = self.head
        prev = itr
        found = 0
        while itr:
            if itr.data == data:
                prev.next = itr.next
                if itr.next:
                    itr.next.prev = prev
                found = 1
                break
            prev = itr
            itr = itr.next
        if found == 0:
            # raise Exception('Data not found')
            pass

    def print_forward(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '<-->'
            itr = itr.next

        print(llstr)
    
    def print_backward(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        llstr = ""
        itr = self.head
        rti=None
        while itr:
            rti = itr
            itr = itr.next
        while rti:
            llstr += str(rti.data) + '<-->'
            rti = rti.prev

        print(llstr)
            


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at_end("dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()