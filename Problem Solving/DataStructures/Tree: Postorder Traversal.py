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
# Recursive
def postOrder(root):
    if root == None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.info, end=' ')

# Iterative
def postOrder(root):
    stack = []
    stack.append(root)
    rslt = []
    
    while stack != []:
        cur = stack.pop(-1)
        rslt.append(cur.info)
        
        if cur.left != None:
            stack.append(cur.left)
        
        if cur.right != None:
            stack.append(cur.right)
    
    rslt.reverse()
    
    for elem in rslt:
        print(elem, end=' ')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

postOrder(tree.root)
