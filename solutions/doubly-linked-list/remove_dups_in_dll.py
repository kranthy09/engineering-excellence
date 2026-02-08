"""
Remove Duplicates in Doubly Linked List

Given a doubly linked list, remove duplicates from it. The list is sorted.

i/o: 1 <-> 2 <-> 2 <-> 4 <-> 5
o/p: 1 <-> 2 <-> 4 <-> 5

Approaches:
1. Straigh forward: Create a new node for each element and link them together.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def from_arr(self, arr):
        """
        Create Doubly Linked List from array of elements.

        TC: O(n)
        AS: O(n)
        """
        n = len(arr)
        # base case

        self.head = Node(arr[0])
        curr = self.head
        for i in range(1, n):
            data_node = Node(arr[i])
            curr.next = data_node
            data_node.prev = curr
            curr = curr.next
        return self.head

    def print_(self, head):
        """
        Prints elements in Doubly LinkedList

        TC: O(n)
        AS: O(1)
        """
        curr = head
        print(None, end=" <- ")
        while curr:
            print(curr.data, end=" ")
            if curr.next:
                print("<-> ", end="")
            curr = curr.next
        print("-> None")

    def remove_duplicates_two_nodes_once(self, head):
        """
        Remove duplicates from sorted Doubly Linked list.

        For each node is same as next node, connect them to next of next node.

        TC: O(n)
        AS: O(1)
        """
        curr = head
        while curr and curr.next:

            # equal nodes
            if curr.data == curr.next.data:
                next_node = curr.next.next
                # linked to it next of next node
                curr.next = next_node
                # handle next node is null
                if next_node:
                    next_node.prev = curr
            else:
                # skip to next node if not duplicate
                curr = curr.next
        return head

    def remove_duplicates_sorted_dll_iterative(self, head):
        """
        Remove duplicates from sorted Doubly Linked list.

        Move a pointer in forward direction, when a duplicate is found skip
        the nodes, and for a non duplicate node, link it with the previous
        non duplicate node.

        TC: O(n)
        AS: O(1)
        """
        curr = head
        temp = head
        while temp:

            # check for non equal nodes
            if curr.data != temp.data:

                # link to its node
                curr.next = temp

                # non equal node points to current node
                # handle if node is null
                if temp and temp.prev:
                    temp.prev = curr

                # move current node to non duplicate node
                curr = temp
                temp = temp.next
            else:
                # move to next node if duplicate
                temp = temp.next
        # if last node is a duplicate, curr will be at last non duplicate node
        if curr.next:
            # link it to null
            curr.next = None
        return head

    def remove_duplicates_sorted_dll_expected(self, head):
        """
        Remove duplicates from sorted Doubly Linked list.

        for each node, move a pointer from next to it, till the
        next node is not a duplicate. Then link the node
        with the next non duplicate node.

        TC: O(n)
        AS: O(1)
        """

        curr = head
        while curr:
            # take next node
            temp = curr.next
            # move temp till the next node is not a duplicate
            while temp and curr.data == temp.data:
                temp = temp.next
            # link to next non duplicate node
            curr.next = temp

            # link non duplicate node to current node
            # handle next node is null
            if temp:
                temp.prev = curr
            # move current node to skill duplicates
            curr = temp
        return head


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 4, 5, 5, 5, 5]
    dll = DoublyLinkedList()
    head = dll.from_arr(arr)
    dll.print_(head)
    head = dll.remove_duplicates_sorted_dll_expected(head)
    dll.print_(head)
