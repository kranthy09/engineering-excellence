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

    def get_middle(self, head_):
        """
        TC: O(n)
        AS: O(1)
        """
        slow = head_
        fast = self.head
        while (fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def is_palindrome(self):
        """
        TC: O(n)
        AS: O(n), recursive call stack
        """
        state = {"is_pal": True}
        self.is_palindrome_recr(self.head, state)
        return state["is_pal"]

    def is_palindrome_recr(self, curr, state):
        """
        Recursive method to check ll palindrome.
        """
        # base condition
        if curr is None:
            return self.head

        front = self.is_palindrome_recr(curr.next, state)
        if curr.data != front.data:
            state["is_pal"] = False
        return front.next

    def is_palindrome_rev(self):
        """
        TC:
        AS:
        """
        if self.head is None:
            return True
        middle = self.get_middle(self.head)
        head1 = self.head
        head2 = middle.next
        middle.next = None
        head2 = self.reverse_linkedlist(head2)
        self.print_elements(head1)
        self.print_elements(head2)
        while head1 is not None and head2 is not None:
            if head1.data != head2.data:
                return False
            head1 = head1.next
            head2 = head2.next
        return True


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    ll = LinkedList()
    ll.from_list(arr)
    print(ll.is_palindrome())
    print(ll.is_palindrome_rev())
