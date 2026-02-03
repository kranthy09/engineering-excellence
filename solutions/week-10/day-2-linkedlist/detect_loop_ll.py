"""
Detect and remove loop in Circular linkedlist
- Floyd's Cycle Detection Algorithm

i/o: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 8 -> 9
               \---<--------------------|
o/p: True

Approaches:
1. Brute Force: Store nodes in hashmap
2. Runner Algorithm:

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def from_list(self, data_list):
        """
        TC: O(n)
        AS: O(1)
        """
        if not data_list:
            return None

        # Create the head node
        self.head = Node(data_list[0])
        current = self.head

        # Iterate through the rest of the list and link nodes
        for value in data_list[1:]:
            current.next = Node(value)
            current = current.next
        current.next = self.head.next

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

    def brute_force_detect_loop(self):
        """
        TC: O(n)
        AS: O(n), for maintaing nodes in hashmap
        """
        hmap = {}
        curr = self.head
        while curr is not None:
            if hmap.get(curr):
                return True
            else:
                hmap[curr] = 1
            curr = curr.next
        return False

    def runner_algo_detect_loop(self):
        """
        TC: O(n)
        AS: O(1)
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def brute_force_remove_loop(self):
        """
        TC: O(n)
        AS: O(n), hashmap for maintaing nodes
        """
        hmap = {}
        curr = self.head
        while curr is not None:
            if hmap.get(curr.next):
                curr.next = None
                return self.head
            else:
                hmap[curr] = 1
            curr = curr.next
        return self.head

    def runner_algo_remove_loop(self):
        """
        TC: O(n)
        AS: O(1)
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return
        # meeting at the head node
        if slow == self.head:
            while slow.next != self.head:
                slow = slow.next
            slow.next = None
            return

        slow = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    ll = LinkedList()
    ll.from_list(arr)
    print(ll.brute_force_detect_loop())
    print(ll.runner_algo_detect_loop())
    head = ll.brute_force_remove_loop()
    ll.print_elements(head)
    ll.runner_algo_remove_loop()
