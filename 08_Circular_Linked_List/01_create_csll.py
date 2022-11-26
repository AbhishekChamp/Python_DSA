# Creation of circular singly linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Circular_Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.tail.next:
                break
        
    # Creation of circular singly linked list
    def create_circular_singly_linked_list(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular Linked List has been created"


circular_singly_linked_list = Circular_Singly_Linked_List()
circular_singly_linked_list.create_circular_singly_linked_list(1)

print([node.value for node in circular_singly_linked_list])