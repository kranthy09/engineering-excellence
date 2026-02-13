"""
First Circular Tour

Given a circular route with N petrol pumps, where each petrol
pump has a certain amount of petrol and is at a certain distance
from the next petrol pump, find the starting petrol pump's
index from which a truck can complete the circular tour
without running out of petrol.

i/o: petrol = [4, 6, 7, 4], distance = [6, 5, 3, 5]
o/p: 1

i/o: petrol = [1, 2, 3, 4], distance = [2, 3, 4, 5]
o/p: -1
"""


class Solution:

    def brute_force(self, petrol, distance):
        """
        For each petrol pump, check whether the truck can
        complete the circular tour.

        TC: O(n^2)
        AS: O(1)
        """
        n = len(petrol)
        for start in range(n):
            fuel = 0
            completed = True
            for i in range(n):
                idx = (start + i) % n
                fuel += petrol[idx] - distance[idx]
                if fuel < 0:
                    completed = False
                    break
            if completed:
                return start
        return -1

    def circular_tour_deque(self, petrol, distance):
        """
        Use a deque to keep track of the petrol pumps and the fuel.

        TC: O(n)
        AS: O(n)
        """
        from collections import deque
        n = len(petrol)
        d = deque()
        size_ = 0
        curr_petrol = 0
        i = 0
        while True:
            curr_petrol += (petrol[i] - distance[i])
            if curr_petrol >= 0:
                d.append(i)
                size_ += 1
            else:
                while d and curr_petrol < 0:
                    inx = d.popleft()
                    size_ -= 1
                    curr_petrol -= (petrol[inx] - distance[inx])
            if size_ == n:
                break
            i = (i + 1) % n
        if curr_petrol >= 0:
            return d[0] + 1
        else:
            return -1


if __name__ == "__main__":
    S = Solution()
    petrol = [4, 6, 7, 4]
    distance = [6, 5, 3, 5]
    print(S.brute_force(petrol, distance))
    print(S.circular_tour_deque(petrol, distance))
