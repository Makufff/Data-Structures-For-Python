# Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# singly-linklist
class singly_Linklist :
    # init
    def __init__(self):
        self.head = None
        
    # is_emtpy()
    def is_empty(self):
        if self.head == None:
            return True
        return False
    
    # append() # add to the end
    def append(self, value):
        new_node = Node(value)
        # if the linklist is empty
        if self.head == None:
            self.head = new_node
        # if the linklist is not empty
        current_node = self.head
        while current_node.next :
            current_node = current_node.next
        current_node.next = new_node

    # prepend() # add to the start
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # delete() # delete a node
    def delete(self, value):

        # if the linklist is empty
        if self.head == None:
            print("list is empty")
            return
        
        # if the linklist is not empty
        # if the head is the node to be deleted
        if self.head.value == value :
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next.value != value and current_node.next :
            current_node = current_node.next
        
        if current_node.next == None:
            print("Node not found")
            return
        
        current_node.next = current_node.next.next

    # Print() # print the linklist
    # output: 1 -> 2 -> 3 -> 4 -> 5 -> None
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    # serach(index) # search a node by index
    # insert(index, value) # insert a node at index
    # delete(index) # delete a node by index
