"""
Add Number Linked Lists


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

    def addTwoLists(self, head1, head2):
        # code here
        state = {"ans": 0, "r": 0}
        self.addTwoListsUtil(head1, head2, state)
        return state["ans"]

    def addTwoListsUtil(self, head1, head2, state):
        """
        """
        # base case
        if head1 is None and head2 is None:
            return
        elif head1 is None:
            # add head2 to end
            temp = 0
            i = 0
            curr = head2
            while curr is not None:
                temp = (10 ** i)*temp + curr.data
                curr = curr.next
                i += 1
            state["ans"] = temp
            state["r"] = i
            print("base: ", state["ans"], state["r"])
            return
        elif head2 is None:
            # add head1 to end
            temp = 0
            i = 0
            curr = head1
            while curr is not None:
                temp = (10 ** i)*temp + curr.data
                curr = curr.next
                i += 1
            state["ans"] = temp
            state["r"] = i
            return

        self.addTwoListsUtil(head1.next, head2.next, state)

        # add head1, head2
        a = head1.data
        b = head2.data
        val = a * (10 ** state["r"]) + b * (10 ** state["r"])
        # update state
        state["ans"] += val
        if (state["ans"]//(10**(state["r"]))) > 9 or a + b < 9:
            state["r"] += 1

        return


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 4, 5, 3]
    arr_ = [3, 4, 6, 8, 9, 3]
    ll = LinkedList()
    head1 = ll.from_list(arr)
    head2 = ll.from_list(arr_)
    ll.print_elements(head1)
    ll.print_elements(head2)
    ans = ll.addTwoLists(head1, head2)
    print(ans)
