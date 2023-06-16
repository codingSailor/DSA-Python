
# Time complexity O(log(n)) - Search/Access/Insert/Delete

class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, value):
        print('hahah',self.data)
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else: 
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
            
    def find_min(self):

        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        elements = self.in_order_traversal()

        return sum(elements)
    
    # LMR inorder
    
    # MLR preoreder

    # LRM postorder

    def post_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)


        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)
        #visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        #visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        
        return self
        
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17,4,1,20,9,23,18,34]

numbers_tree = build_tree(numbers)

print(numbers_tree.in_order_traversal())
# print(numbers_tree.post_order_traversal())
# print(numbers_tree.pre_order_traversal())
# print(numbers_tree.calculate_sum())
# print(numbers_tree.find_max())
# print(numbers_tree.find_min())

# print(numbers_tree.search(24))
print(numbers_tree.delete(9))
print(numbers_tree.delete(20))
print(numbers_tree.delete(9))
print(numbers_tree.in_order_traversal())


