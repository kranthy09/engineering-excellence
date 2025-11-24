"""
We are given an integer array asteroids of size N
representing asteroids in a row. For each asteroid,
the absolute value represents its size, and the sign
represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the
same speed. Find out the state of the asteroids after
all collisions. If two asteroids meet, the smaller
one will explode. If both are of the same size,
both will explode. Two asteroids moving in the same direction will never meet.
"""


class AstriodCollisions:

    def __init__(self, arr):
        self.arr = arr

    def brute_force(self):
        """
        scan the array for collision exists,
        if the collision exists remove/modify those elements
        and again scan the array till there are no collisions
        found.
        TC: O(n^2)
        SC: O(n)
        """
        while True:
            collision_found = False
            new_astroids = []
            i = 0
            while i < len(self.arr):
                if (
                    i + 1 < len(self.arr)
                    and self.arr[i] > 0
                    and self.arr[i + 1] < 0
                ):
                    collision_found = True
                    left_size = self.arr[i]
                    right_size = abs(self.arr[i + 1])
                    if left_size > right_size:
                        new_astroids.append(self.arr[i])
                        collision_found = True
                        i += 2
                    elif left_size < right_size:
                        new_astroids.append(self.arr[i + 1])
                        collision_found = True
                        i += 2
                    else:
                        i += 2
                        collision_found = True
                else:
                    new_astroids.append(self.arr[i])
                    i += 1
            self.arr = new_astroids
            if not collision_found:
                break
        return self.arr

    def expected_approach(self):
        """
        consider a stack, and append the elements in to the stack
        of moving same direction, if there is opposite sign occurs
        check with top element in the stack, continue till all
        the elements in the arr are completed.
        TC: O(n)
        SC: O(n)
        """
        stack = []
        n = len(self.arr)
        for i in range(n):
            while stack and stack[-1] > 0 and self.arr[i] < 0:
                # collision found
                if stack[-1] < abs(self.arr[i]):
                    stack.pop()
                    continue
                elif stack[-1] == abs(self.arr[i]):
                    stack.pop()
                break
            else:
                stack.append(self.arr[i])
        return stack


if __name__ == "__main__":
    arr = [3, 5, -3]
    res = AstriodCollisions(arr)
    print(res.brute_force())
    print(res.expected_approach())
