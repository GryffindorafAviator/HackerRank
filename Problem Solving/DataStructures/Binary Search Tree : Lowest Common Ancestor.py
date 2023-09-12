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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
# Solution 1
def lca(root, v1, v2):
    node = root
    
    while node != None:
        if node.info > v1 and node.info > v2:
            node = node.left
        elif node.info < v1 and node.info < v2:
            node = node.right
        else:
            return node

# Solution 2
def lca(root, v1, v2):
    if root == None:
        return root
    
    if root.info == v1 or root.info == v2:
        return root
    
    left = lca(root.left, v1, v2)
    right = lca(root.right, v1, v2)
    
    if left != None and right != None:
        return root
    
    return left if left != None else right

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
