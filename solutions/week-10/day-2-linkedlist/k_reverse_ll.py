"""
Check if linkedlist is a palindrome

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
        while current is not None:
            print(current.data, end=" --> ")
            current = current.next
        print("None")
        return

    def reverse_linkedlist(self, head_):
        """
        TC: O(n)
        AS: O(1)
        """
        print("reverse: ")
        prev = None
        curr = head_
        while curr is not None:
            # preserve forward linking
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def k_reverse_recr(self, head, k):
        """
        TC:
        AS:
        """
        """
        Reverse k length in linkedlist, recursively
        """
        # base case
        if head is None or k <= 1:
            return head
        cnt = 0
        prev = None
        curr = head
        last = head
        while curr is not None and cnt < k:
            # preserve forward linking
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            cnt += 1
        last.next = self.k_reverse_recr(curr, k)
        return prev


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ll = LinkedList()
    head = ll.from_list(arr)
    rev = ll.k_reverse_recr(head, 3)
    ll.print_elements(rev)
