class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        new_node = Node(val)
        
        if self.root == None:
            self.root = new_node
        else:
            prv = None
            cur = self.root
            
            while cur != None:
                prv = cur
                
                if val < cur.info:
                    cur = cur.left
                else:
                    cur = cur.right
            
            if val < prv.info:
                prv.left = new_node
            else:
                prv.right = new_node
        
        return self.root
                    
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
