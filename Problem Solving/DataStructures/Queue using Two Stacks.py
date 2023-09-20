stack1 = []
stack2 = []

def enqueue(x):
    stack1.append(x)

def dequeue():
    if stack2 == []:
        while stack1 != []:
            stack2.append(stack1.pop(-1))
    
    stack2.pop(-1)

def printElem():
    if stack2 == []:
        while stack1 != []:
            stack2.append(stack1.pop(-1))
    
    print(stack2[-1])

nq = int(input())

for _ in range(nq):
    command = list(map(int, input().split(' ')))
    
    if command[0] == 1:
        enqueue(command[1])
    elif command[0] == 2:
        dequeue()
    else:
        printElem()
