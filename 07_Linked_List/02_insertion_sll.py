
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

single_link_list  = Single_Liked_List()
print(node.value for node in single_link_list)  