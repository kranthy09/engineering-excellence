"""
Problem Statement: Implement a singly linked list with the following methods:

1. Insert an element at the begining of linked list
2. Print elements in linked list
3. Insert at the end
4. Insert at the position
5. Delete at the begining.
6. Delete at the end.
7. Delete at position
8. Reverse Linkedlist
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        if node is not None:
            self.head = node
        else:
            self.head = None

    def insert_at_beginning(self, data):
        """
        TC: O(1)
        AS: O(1)
        """
        print("insert at begin")
        # base case
        if self.head is None:
            self.head = Node(data)
            return self.head.data
        data_node = Node(data)
        data_node.next = self.head
        self.head = data_node
        return self.head.data

    def print_elements(self):
        """
        TC: O(n)
        AS: O(1)
        """
        print("print: ")
        # base case
        if self.head is None:
            print(self.head)
            return
        current = self.head
        while current is not None:
            print(current.data, end=" --> ")
            current = current.next
        print("None")
        return

    def insert_at_end(self, data):
        """
        TC: O(n)
        AS: O(1)
        """
        print("insert at end: ")
        # base case
        if self.head is None:
            self.insert_at_beginning(data=data)
            return

        data_node = Node(data=data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = data_node

    def insert_at_position(self, position, data):
        """
        TC: O(n)
        AS: O(1)
        """
        print("insert at pos: ")
        # base case
        if (position <= 0 or self.head is None):
            self.insert_at_beginning(data=data)
            return

        curr = self.head
        hops = 0
        while hops < position - 1 and curr.next is not None:
            curr = curr.next
            hops += 1
        data_node = Node(data=data)
        curr_next = curr.next
        curr.next = data_node
        data_node.next = curr_next
        return

    def delete_at_beginning(self):
        """
        TC: O(1)
        AS: O(1)
        """
        print("delete at begin")
        # base case
        if self.head is None:
            return

        # Just point the head to the next node
        # The old head node's reference count drops to 0
        self.head = self.head.next

        # Python's GC will automatically free the memory
        # of the old head when it's no longer reachable.

    def delete_at_end(self):
        """
        TC: O(n)
        AS: O(1)
        """
        print("delete at end")
        # base case
        if self.head is None:
            return

        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def delete_at_position(self, position):
        """
        TC: O(n)
        AS: O(1)
        """
        print("delete at pos")
        # base case
        if position <= 0 or self.head is None:
            return

        curr = self.head
        hops = 0
        while hops < position - 1 and curr.next.next is not None:
            curr = curr.next
        next_ = curr.next
        curr.next = next_.next

    def reverse_linkedlist(self):
        """
        TC: O(n)
        AS: O(1)
        """
        print("reverse: ")
        prev = None
        curr = self.head
        while curr is not None:
            # preserve forward linking
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def get_middle(self):
        """
        TC:
        AS:
        """
        slow = self.head
        fast = self.head
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow.data


if __name__ == "__main__":
    node = Node(1)
    ll = LinkedList(node)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(5)
    ll.print_elements()
    ll.insert_at_end(4)
    ll.print_elements()
    ll.insert_at_position(1, 10)
    ll.print_elements()
    ll.delete_at_beginning()
    ll.print_elements()
    ll.delete_at_end()
    ll.print_elements()
    ll.delete_at_position(2)
    ll.print_elements()
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.insert_at_end(8)
    ll.insert_at_end(9)
    ll.print_elements()
    ll.reverse_linkedlist()
    ll.print_elements()
    print("middle: ", ll.get_middle())
    ll.insert_at_position(3, 15)
    ll.insert_at_position(3, 25)
    ll.insert_at_position(3, 45)
    ll.print_elements()
    print("middle: ", ll.get_middle())
