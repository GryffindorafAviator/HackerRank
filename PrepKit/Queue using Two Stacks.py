class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, element):
        self.in_stack.append(element)
    
    def dequeue(self):
        if self.out_stack == []:
            while self.in_stack != []:
                self.out_stack.append(self.in_stack.pop(-1))
        
        if self.out_stack != []:
            self.out_stack.pop(-1)
        else:
            return None
    
    def print_element(self):
        if self.out_stack == []:
            while self.in_stack != []:
                self.out_stack.append(self.in_stack.pop(-1))
        
        if self.out_stack != []:
            p = self.out_stack.pop(-1)
            self.out_stack.append(p)
            print(p)
        else:
            print("None")

q = int(input())
queue = Queue()

for _ in range(q):
    query = list(map(int, input().split(' ')))
    
    if query[0] == 1:
        queue.enqueue(query[1])
    elif query[0] == 2:
        queue.dequeue()
    else:
        queue.print_element()
