class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, value):
        fname = self.data.split()

        spaces = ' ' * self.get_level() *4
        prefix = spaces + '|__' if self.parent else ''
        if value == 'both':
            print(prefix + self.data)
        elif value == 'names':
            print(prefix + fname[0])
        elif value == 'desig':
            print(prefix + self.designation)
        else:
            print('Invalid value')
        if self.children:
            for child in self.children:
                child.print_tree(value)

    def get_level(self):
        level = 0
        p =self.parent
        while p:
            level += 1
            p = p.parent
        return level


# def build_tree():
#     root = TreeNode("Electronics")

#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))
    
#     cellphone = TreeNode("cellphone")
#     cellphone.add_child(TreeNode("iphone"))
#     cellphone.add_child(TreeNode("Pixel"))
#     cellphone.add_child(TreeNode("Oneplus"))

#     tv = TreeNode("tv")
#     tv.add_child(TreeNode("LG"))
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("Onida"))
    
#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)

#     # print(tv.get_level())
#     return root

# root = build_tree()

# root.print_tree()

def office_tree():
    root = TreeNode("Nilupul (CEO)", '(CEO)')

    cto = TreeNode("Chinmay (CTO)", '(CTO)')
    infra = TreeNode("Vishwa (Infra Head)","(Infra Head)")
    cto.add_child(infra)
    infra.add_child(TreeNode("Dhaval (Cloud)", "(Cloud)"))
    infra.add_child(TreeNode("Abhijit (App Manager)", "(App Manager)"))
    
    cto.add_child(TreeNode("Aamir (App Head)", "(App Head)"))
    
    hr = TreeNode("Gels (HR head)", "(HR head)")
    hr.add_child(TreeNode("peter (Recruter)", "(Recruter)"))
    hr.add_child(TreeNode("Waqas (Policy)", "(Policy)"))
    
    root.add_child(cto)
    root.add_child(hr)

    # print(tv.get_level())
    return root

office = office_tree()

office.print_tree('both')
office.print_tree('names')
office.print_tree('desig')
