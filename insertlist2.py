class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: any):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def swap_nodes(self, key_1: any, key_2: any):
        if key_1 == key_2:
            return
        
        prev_1, curr_1 = None, self.head
        prev_2, curr_2 = None, self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            print(f"Swapping not possible: One or both keys ({key_1}, {key_2}) not found")
            return