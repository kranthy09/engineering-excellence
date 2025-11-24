"""
You have been given a land in the form of an array of size n.
On each index, there is a king who wants to determine its
property. Land at each index has some value. Every king
considers every land to its left and right his property
until he does not see land of value bigger than his.
Note that the value of individual land does not change
based on the consideration of kings. You have to print
the value of land that each king considers to be his.
"""


class KingsLand:

    def __init__(self, land_values):
        self.land_values = land_values

    def brute_force(self):
        """
        for each i, add the land_values that
        king can span untill land greater then him pn right
        and left.
        TC: O(n^2)
        SC: O(n)
        """
        n = len(self.land_values)
        res = [0] * n
        for i in range(n):
            # Go right
            res[i] = land_values[i]
            if i < n:
                for j in range(i+1, n):
                    if land_values[i] < land_values[j]:
                        break
                    else:
                        res[i] += land_values[j]
            # Go left
            if i > 0:
                for k in range(i-1, -1, -1):
                    if land_values[i] < land_values[k]:
                        break
                    else:
                        res[i] += land_values[k]
        return res

    def expected_approach(self):
        """
        consider monotonically decreasing stack,
        for each i, find the right index that can span
        until greater than land_value at i and
        find the left index that can span until greater
        than land_values at i.
        TC:
        SC:
        """
        n = len(self.land_values)
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and self.land_values[stack[-1]] < self.land_values[i]:
                inx = stack.pop()
                right[inx] = i
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and self.land_values[stack[-1]] < self.land_values[i]:
                inx = stack.pop()
                left[inx] = i
            stack.append(i)
        res = [0] * n
        for i in range(n):
            res[i] = sum([self.land_values[k]
                         for k in range(left[i]+1, right[i])])

        return res


if __name__ == "__main__":
    land_values = [4, 3, 5, 1, 2]
    res = KingsLand(land_values)
    print(res.brute_force())
    print(res.expected_approach())
