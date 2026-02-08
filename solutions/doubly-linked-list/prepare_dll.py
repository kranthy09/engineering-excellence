"""
Prepare Doubly Linked List with array of elements.


i/o: [1, 2, 3, 4, 5]
o/p: None <- 1 <-> 2 <-> 3 <-> 4 <-> 5 -> None

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
        """
        curr = head
        print(None, end=" <- ")
        while curr:
            print(curr.data, end=" ")
            if curr.next:
                print("<-> ", end="")
            curr = curr.next
        print("-> None")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    dll = DoublyLinkedList()
    head = dll.from_arr(arr)
    dll.print_(head)
