
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

class Single_Liked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # Insert to Single Linked List
    def insertSLL(self, value, location):
        new_node = Node(value)
        if self.head is None and location == 0:
            self.head = new_node
            self.tail = new_node
        elif self.head is None and location != 0:
            print(f"Trying to access position {location} in an empty linked list.")
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
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
                    else:
                        print(f"Position {location} is out of range in linked list of size {index}")

    # Traverse Single Linked List
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search in a single Linked List
    def searchSLL(self, node_value):
        if self.head is None:
            return "The List does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == node_value:
                    return node.value
                node = node.next
            return "The value does not exist in the list"

    # Delete a node from Single Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("The Single List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            else:
                tempnode = self.head
                index = 0
                try:
                    while index < location - 1:
                        tempnode = tempnode.next
                        index += 1
                    if tempnode.next == self.tail:
                        tempnode.next = None
                        self.tail = tempnode
                    else:
                        next_node = tempnode.next
                        tempnode.next = next_node.next
                except:
                    print(f"Index {location} out of list")


    

def show_result():
    print("Single Linked List : ", end="")
    print([node.value for node in single_link_list])

print("Insertion Linked List")
print("-----------------------------------------")
single_link_list  = Single_Liked_List()
# Insert value at position 2 -> Will cause error
single_link_list.insertSLL(3, 2)
show_result()
# Insert value at position 0
single_link_list.insertSLL(1, 0)
show_result()
# Insert value at position 1
single_link_list.insertSLL(2, 1)
show_result()
# Insert value at position 5 -> Will cause error
single_link_list.insertSLL(0, 5)
show_result()
# Insert value at position 0
single_link_list.insertSLL(0, 0)
show_result()
# Insert value at position 1
single_link_list.insertSLL(30, 1)
show_result()
# Insert value at position 2
single_link_list.insertSLL(32, 2)
show_result()
# Insert value at position -1  -> Will cause error
single_link_list.insertSLL(50, -1)
# Traverse Linked List
print("-----------------------------------------")
print("Traverse Linked List")
single_link_list.traverseSLL()
# Search Linked List
print("-----------------------------------------")
print("Search Linked List")
print(single_link_list.searchSLL(30))
# Deleting Single Linked List
print("-----------------------------------------")
print("Deleting Linked List")
single_link_list.deleteNode(4)
show_result()
single_link_list.deleteNode(0)
show_result()
single_link_list.deleteNode(1)
show_result()
single_link_list.deleteNode(4)
show_result()