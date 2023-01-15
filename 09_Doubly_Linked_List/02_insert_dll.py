# Inserting Doubly Linked List

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The Double Linked List is created Successfully"
    
    # Insertion Method in Doubly Linked List
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be empty")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                newNode.next = newNode

doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)
print([node.value for node in doublyLL])

doublyLL.insertNode(0, 0)
print([node.value for node in doublyLL])
doublyLL.insertNode(2, 1)
print([node.value for node in doublyLL])
doublyLL.insertNode(6, 1)
print([node.value for node in doublyLL])