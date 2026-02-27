class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Singlyll:
    def __init__(self):
        self.head=None
    
    def insert_beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    
    def insert_end(self,data):
        ne=Node(data)
        if self.head is None:
            self.ne=None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp=self.head
            while temp:
                print(f"{temp.data}-->",end="")
                temp=temp.next
            print("None")

l=Singlyll()
l.insert_beg(30)
l.insert_beg(20)
l.insert_beg(10)

print("Initial list")
l.display()

print("Iserting 100 at beginning")
l.insert_beg(100)
l.display()

print("Inserting 500 at end")
l.insert_beg(500)
l.display()