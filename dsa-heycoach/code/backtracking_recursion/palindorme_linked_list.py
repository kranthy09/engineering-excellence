"""
Given the head of a singly linked list,
return True if it is a palindrome or False otherwise.
"""

from typing import List, Optional


class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class CheckPalindromeLinkedList:
    def __init__(self, nodes: List[LinkedList]):
        # Expecting list of nodes, but we need the head (first node)
        self.head = nodes[0] if nodes else None
        self.front_pointer = self.head

    def brute_force(self):
        """
        Brute Force Approach:
        Convert the linked list into a list of values,
        then check if the list is equal to its reverse.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values == values[::-1]

    def expected_approach(self):
        """
        Recursive Approach:
        Use recursion to traverse to the end of the list.
        During the unwinding phase, compare the current node’s value
        (from the end) with the front pointer’s value (from the start).
        Move the front pointer forward after each comparison.
        """

        def check(current: Optional[LinkedList]) -> bool:
            # Base case: reached the end of the list
            if current is None:
                return True

            # Recurse deeper
            if not check(current.next):
                return False

            # Compare the front and current nodes
            if self.front_pointer.val != current.val:
                return False

            # Move the front pointer forward
            self.front_pointer = self.front_pointer.next
            return True

        return check(self.head)


if __name__ == "__main__":
    # Example: Palindrome linked list 1 -> 2 -> 2 -> 1
    node4 = LinkedList(1)
    node3 = LinkedList(2, next=node4)
    node2 = LinkedList(2, next=node3)
    node1 = LinkedList(1, next=node2)
    nodes = [node1, node2, node3, node4]

    res = CheckPalindromeLinkedList(nodes)

    print("Brute Force Result:", res.brute_force())        # True
    print("Expected (Recursive) Result:", res.expected_approach())  # True
