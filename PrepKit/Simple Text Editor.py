class Editor:
    def __init__(self):
        self.s = ""
        self.edit_history = []
    
    def append(self, string):
        self.edit_history.append(("append", len(string)))
        self.s += string
    
    def delete(self, k):
        self.edit_history.append(("delete", self.s[-k:]))
        self.s = self.s[:len(self.s) - k]
    
    def print_char(self, k):
        print(self.s[k])
    
    def undo(self):
        last_edit = self.edit_history.pop(-1)
        
        if last_edit[0] == "append":
            self.s = self.s[:len(self.s) - last_edit[1]]
        else:
            self.s += last_edit[1]

editor = Editor()

q = int(input())

for i in range(q):
    op = input().split()
    
    if op[0] == '1':
        editor.append(op[1])
    elif op[0] == '2':
        editor.delete(int(op[1]))
    elif op[0] == '3':
        editor.print_char(int(op[1]) - 1)
    else:
        editor.undo()
