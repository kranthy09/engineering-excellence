"""
Given the head of a singly linked list,
reverse the list, and return the reversed list.
"""

from typing import List


class LinkedList:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseLinkedList:

    def __init__(self, nodes: List[LinkedList]):
        self.head = nodes[0] if nodes else None

    def brute_force(self):
        """
        append values to a list and reverse using slicing operator
        """
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res[::-1]

    def expected_approach(self):
        """
        Go deep into the last node and reverse the linking
        """

        def reverseList(head_node):
            """
            description: Reverses linkedlist by assigning head to last node
            and reverse the linking between nodes
            """
            if not head_node or not head_node.next:
                return head_node

            reversed_head = reverseList(head_node.next)
            head_node.next.next = head_node
            head_node.next = None

            return reversed_head
        curr = reverseList(self.head)
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


if __name__ == "__main__":
    node4 = LinkedList(5)
    node3 = LinkedList(4, next=node4)
    node2 = LinkedList(3, next=node3)
    node1 = LinkedList(2, next=node2)
    node0 = LinkedList(1, next=node1)
    nodes = [node0, node1, node2, node3, node4]

    res = ReverseLinkedList(nodes)

    print("Brute Force Result:", res.brute_force())
    print("Expected (Recursive) Result:", res.expected_approach())
