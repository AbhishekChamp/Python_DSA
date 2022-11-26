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
            if node.next == self.tail.next:
                break
            node = node.next
        
    # Creation of circular singly linked list
    def create_circular_singly_linked_list(self, node_value):
        if self.head is None:
            node = Node(node_value)
            node.next = node
            self.head = node
            self.tail = node
            return "The Circular Singly Linked List has been created"
        else:
            print("Circular Singly Linked List is already created")
            return "Circular Singly Linked List is already created"

    # Insertion of a node in circular singly linked list
    def insert_circular_singly_linked_list(self, value, location):
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
                self.tail.next = new_node
            else:
                temp_node = self.head
                index = 1
                if index > location:
                    print(f"Invalid position {location} in linked list")
                else:
                    flag = True
                    while index < location:
                        temp_node = temp_node.next
                        if temp_node == self.tail.next:
                            flag = False
                            break
                        index += 1
                    if flag:
                        next_node = temp_node.next
                        temp_node.next = new_node
                        new_node.next = next_node
                        if temp_node == self.tail:
                            self.tail = new_node
                            self.tail.next = self.head
                    else:
                        print(f"Position {location} is out of range in circular linked list of size {index}")

    # Traversal of a node in circular singly linked list
    def traversal_circular_singly_linked_list(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break

circular_singly_linked_list = Circular_Singly_Linked_List()
circular_singly_linked_list.create_circular_singly_linked_list(1)
circular_singly_linked_list.insert_circular_singly_linked_list(2, 0)
circular_singly_linked_list.insert_circular_singly_linked_list(3, -4)
circular_singly_linked_list.insert_circular_singly_linked_list(6, 6)
circular_singly_linked_list.insert_circular_singly_linked_list(3, 2)
circular_singly_linked_list.insert_circular_singly_linked_list(5, 1)
circular_singly_linked_list.create_circular_singly_linked_list(4)
circular_singly_linked_list.traversal_circular_singly_linked_list()


print([node.value for node in circular_singly_linked_list])