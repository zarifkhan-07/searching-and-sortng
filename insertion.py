class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        ne.prev = temp

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end = " ")
                temp=temp.next

n = DoublyLL()
n.head = None

n1 = Node(20)
n2 = Node(1)
n2 = Node(30)

n1.prev = n
n1.next = n2
n1.display()

printEnd=("\n")
n.insert_beg(100)
n.display()

printEnd=("\n")
n.insert_end(100)