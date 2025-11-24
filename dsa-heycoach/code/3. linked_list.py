# create Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create LinkedList class
# LinkedList class maintains the overall
# structure of the linked list

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head:
            current_node = self.head
            while current_node:
                print(current_node.data, end=" ")
                current_node = current_node.next
        else:
            print("The list is empty.")
        print()

    def length(self):
        curr_len = 1
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            curr_len += 1
        return curr_len

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        self.printList()

    def insertAtBegin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.printList()

    def insertAtIndex(self, data, index):
        if self.length == 0:
            self.insertAtBegin(data)
        if self.length() > index:
            curr_inx = 0
            curr_node = self.head
            node = Node(data)
            while curr_inx + 1 < index:
                curr_node = curr_node.next
                curr_inx += 1

            node.next = curr_node.next
            curr_node.next = node
        else:
            self.insertAtEnd(data)

        self.printList()

    def updateNode(self, data, index):
        if index < 0 or index > self.length():
            print("Index out of range")
            return
        curr_inx = 0
        curr_node = self.head
        while curr_inx < index:
            curr_node = curr_node.next
            curr_inx += 1
        curr_node.data = data
        self.printList()

    def removeFirstNode(self):
        if self.head is None:
            print("No nodes available")
        else:
            self.head = self.head.next
        self.printList()

    def remove_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        else:
            curr_inx = 0
            curr_node = self.head
            while curr_inx + 2 < self.length():
                curr_node = curr_node.next
                curr_inx += 1
            curr_node.next = None
        self.printList()

    def remove_at_index(self, index):
        if index < 0 or index > self.length():
            print("Index not present")
        if self.head is None:
            return
        curr_inx = 0
        curr_node = self.head
        while curr_inx + 1 < index:
            curr_node = curr_node.next
            curr_inx += 1
        curr_node.next = curr_node.next.next
        self.printList()

    def remove_node(self, data):
        if self.head is None:
            return
        if self.head == data:
            self.head = None
            return
        if self.head.next == data:
            self.head.next = None
            return
        curr_inx = 0
        curr_node = self.head
        found = False
        while curr_inx + 1 < self.length():
            curr_node = curr_node.next
            if curr_node.data == data:
                found = True
                break
            curr_inx += 1
        if found:
            self.remove_at_index(curr_inx)
        else:
            print("data node not found")
        self.printList()


ll = LinkedList()

# Insert at the end
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(8)
ll.insertAtBegin(3)
ll.insertAtBegin(5)
ll.insertAtIndex(4, 1)
ll.insertAtIndex(9, 6)
ll.updateNode(11, 3)
ll.removeFirstNode()
ll.remove_last_node()
ll.remove_at_index(3)
ll.remove_at_index(1)
ll.remove_node(11)
ll.remove_node(12)
