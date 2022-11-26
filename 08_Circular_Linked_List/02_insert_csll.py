# Circular singly linked list

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

    # Insertion of a node in circular linked list
    def insert_circular_singly_list(self, value, location):
        new_node = Node(value)
        if self.head is None and location == 0:
            self.head = new_node
            self.tail = new_node
        elif self.head is None and location != 0:
            print(f"Trying to access positon {location} in an empty linked list.")
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 1
                if index > location:
                    print(f"Invalid position {location} in linked list")
                else:
                    flag = True
                    try:
                        while index < location:
                            temp_node = temp_node.next
                            index += 1
                    except:
                        flag = False
                    if flag:
                        next_node = temp_node.next
                        temp_node.next = new_node
                        new_node.next = next_node
                        if temp_node == self.tail:
                            self.tail = new_node
                            self.tail.next = self.head
                    else:
                        print(f"Position {location} is out of range in circular linked list of size {index}")

circular_singly_linked_list = Circular_Singly_Linked_List()
# circular_singly_linked_list.create_circular_singly_linked_list(1)
circular_singly_linked_list.insert_circular_singly_list(1, 0)

print([node.value for node in circular_singly_linked_list])