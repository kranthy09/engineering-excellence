"""
Clone Linkedlist
i/o: 9 --> 8 --> 7 --> 6 --> 5 --> 3 --> 10 --> None
o/p: False

i/o: 1 --> 3 --> 6 --> 3 --> 6 --> 1 --> None
o/p: True
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def from_list(self, data_list):
        if not data_list:
            return None

        # Create the head node
        self.head = Node(data_list[0])
        current = self.head

        # Iterate through the rest of the list and link nodes
        for value in data_list[1:]:
            current.next = Node(value)
            current = current.next

        return self.head

    def copy_(self, head):
        """
        Copy of linkedlist by creating new head
        """



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    ll = LinkedList()
    ll.from_list(arr)
