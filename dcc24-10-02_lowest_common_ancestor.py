l = [1,2]
p = 1
q = 2
class Node:
    def __init__(self,val=None,l=None,r=None):
        self.val = val
        self.left = l
        self.right = r
class Tree:
    def __init__(self):
        self.root = None
    def insert(self,v):
        if self.root == None:
            self.root = Node(v)
        else:
            c = self.root
            while c:
                if c.val>v and c.left == None:
                    c.left = Node(v)
                    break
                elif c.val<v and c.right == None:
                    c.right = Node(v)
                    break
                elif c.val>v:
                    c = c.left
                else:
                    c = c.right
t = Tree()
for i in l:
    if i != None:
        t.insert(i)
c = t.root
while c:
    if c.val>p and c.val>q:
        c = c.left
    elif c.val <p and c.val<q:
        c = c.right
    else:
        print(c.val)
        break
