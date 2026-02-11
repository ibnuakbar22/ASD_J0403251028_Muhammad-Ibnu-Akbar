class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
def delete_node(self, key):
    temp = self.head

    if temp and temp.data == key:
        self.head = temp.next
        temp = None
        return 

    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next

    if temp is None:
        return

    prev.next = temp.next
    temp = None