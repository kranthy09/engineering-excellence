"""
Merege Two Sorted Linked Lists

Given the heads of two sorted linked lists,
merge them into one sorted linked list.
The list should be made by splicing together the nodes of the first two lists.

i/o: 1 --> 2 --> 4 --> None
    1 --> 3 --> 4 --> None
o/p: 1 --> 1 --> 2 --> 3 --> 4 --> 4 --> None


Approaches:
1. Brute Force: Create a new linked list and two pointers approach.
2. Expected: In-place merging of two linked lists.

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
    # Merge two sorted linked lists

    def brute_force_merge(self, head1, head2):
        """
        TC: O(n + m)
        AS: O(n + m)
        """
        curr1 = head1
        curr2 = head2
        if curr1.data > curr2.data:
            merge = Node(curr2.data)
            curr2 = curr2.next
        else:
            merge = Node(curr1.data)
            curr1 = curr1.next
        head3 = merge
        while curr1 is not None and curr2 is not None:
            if curr1.data > curr2.data:
                data_node = Node(curr2.data)
                curr2 = curr2.next

            else:
                data_node = Node(curr1.data)
                curr1 = curr1.next
            merge.next = data_node
            merge = merge.next
        print(curr2.data)
        while curr1 is not None:
            merge.next = curr1
            curr1 = curr1.next
            merge = merge.next
        while curr2 is not None:
            merge.next = curr2
            curr2 = curr2.next
            merge = merge.next

        return head3

    def expected_approach_merge(self, head1, head2):
        """
        TC:
        AS:
        """
        curr1 = head1
        curr2 = head2
        prev = head1
        while curr2 is not None and curr1 is not None:
            if curr1.data == curr2.data:
                prev = curr1
                curr1 = curr1.next
            if curr1.data > curr2.data:
                temp1 = curr1.next
                temp2 = curr2.next
                prev.next = curr2
                curr2.next = temp1
                prev = prev.next
                curr2 = temp2
            elif curr1.data < curr2.data:
                temp1 = curr1.next
                temp2 = curr2.next
                curr1.next = curr2
                curr2.next = temp1
                curr2 = temp2
                curr1 = temp1
                prev = prev.next
        return head1

    def merge_recr(self, head1, head2):
        """
        TS: O(n+m)
        AS: O(n+m)
        """
        return self.merge_recr_util(head1, head2)

    def merge_recr_util(self, head1, head2):
        """
        Merge two sorted linkedlist recursively
        """
        # base case
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        if head1.data <= head2.data:
            head1.next = self.merge_recr_util(head1.next, head2)
            return head1
        else:
            head2.next = self.merge_recr_util(head1, head2.next)
            return head2


if __name__ == "__main__":
    arr1 = [1, 1, 2, 3]
    arr2 = [1, 4, 5, 6]
    ll = LinkedList()
    head1 = ll.from_list(arr1)
    head2 = ll.from_list(arr2)
    # head3 = ll.brute_force_merge(head1, head2)
    ll.print_elements(ll.merge_recr(head1, head2))
