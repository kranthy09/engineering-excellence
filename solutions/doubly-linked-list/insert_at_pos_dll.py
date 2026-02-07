"""
Insertion at doubly linked list

Input: p = 2, x = 6
Output: 2 <-> 4 <-> 5 <-> 6

Input: p = 0, x = 44
Output: 1 <-> 44 <-> 2 <-> 3 <-> 4
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
            data_node = Node(value)
            current.next = data_node
            data_node.prev = current
            current = current.next

        return self.head

    def print_elements(self, head_):
        """
        TC: O(n)
        AS: O(1)
        """
        print("print: ")
        # base case
        if head_ is None:
            print(head_)
            return
        current = head_
        previous = head_
        while current is not None:
            print(current.data, end=" --> ")
            previous = current
            current = current.next
        print("None")
        while previous is not None:
            print(previous.data, end=" --> ")
            previous = previous.prev
        print("None")

    def insert_at_pos(self, head, pos, val):
        """
        Insert next to pos-index.
        TC:
        AS:
        """
        data_node = Node(val)
        # base case
        if head is None or pos < 0:
            head = data_node
            return head

        curr = head
        for _ in range(pos):
            if curr.next is None:
                break
            curr = curr.next
        data_node.next = curr.next
        data_node.prev = curr
        if curr.next:
            curr.next.prev = data_node
        curr.next = data_node
        return head


if __name__ == "__main__":
    arr = [1]
    dll = DoublyLinkedList()
    head = dll.from_list(arr)
    dll.print_elements(head)
    head = dll.insert_at_pos(head, 10, 6)
    dll.print_elements(head)
