""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    stack = []
    cur = root
    prv = -1
    
    while cur != None or stack != []:
        if cur != None:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop(-1)
            
            if cur.data <= prv:
                return False
            
            prv = cur.data
            cur = cur.right
        
    return True
            
