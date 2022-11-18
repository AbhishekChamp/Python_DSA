

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class Single_Liked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


single_linked_list = Single_Liked_List()
node1 = Node(1)
node2 = Node(2)

single_linked_list.head = node1
single_linked_list.head.next = node2
single_linked_list.tail = node2