"""
Generate stack from array of elements.
i/o: [1, 2, 3]
o/p: [1, 2, 3]

"""


class Stack:

    def __init__(self):
        self.stack = []
        self._size = 0

    def push(self, element):
        self.stack.append(element)
        self._size += 1

    def pop(self):
        if self._size == 0:
            return None
        self._size -= 1
        return self.stack.pop()

    def peek(self):
        if self._size == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size


if __name__ == "__main__":
    arr = [1, 2, 3]
    s = Stack()
    for element in arr:
        s.push(element)
    print(s.stack)
