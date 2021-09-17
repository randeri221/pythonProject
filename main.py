class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

    def printf(self):
        node = self
        while(node != None):
            print(node.data)
            node = node.next



a = Node(5,Node(10,None))
a.printf()
