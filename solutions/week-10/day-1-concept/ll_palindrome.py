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

    def is_palindrome(self):
        """
        TC:
        AS:
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


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ll = LinkedList()
    ll.from_list(arr)
    print(ll.is_palindrome())
