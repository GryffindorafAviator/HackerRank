class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    def positionBook(book, node, position, level):
        if node == None:
            return
        
        if position in book:
            if book[position][1] > level:
                book.update({position:[node.info, level]})
        else:
            book[position] = [node.info, level]
        
        positionBook(book, node.left, position - 1, level + 1)
        positionBook(book, node.right, position + 1, level + 1)

    book = {}
    positionBook(book, root, 0, 0)
    minimum = 10000
    maximum = -10000
    
    for position in book.keys():
        minimum = min(minimum, position)
        maximum = max(maximum, position)
    
    i = minimum
    
    while i <= maximum:
        print(book[i][0], end=' ')
        i += 1

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
