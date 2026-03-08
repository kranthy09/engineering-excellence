"""
Pythogorean Triplet (Medium)
@topic: potd
@difficulty: medium
@tags: arrays

Given an array arr[], return true if there is a triplet
(a, b, c) from the array (where a, b, and c are on
different indexes) that satisfies a2 + b2 = c2, otherwise return false.

i/o: [3, 2, 4, 6, 5]
o/p: True


Approaches:
1. Expected: find each pair till max of arr and store them in hmap.
"""


class Solution:

    def expected_solution(self):
        """
        TC: O(maxx^2)
        AS: O(maxx), storing max of array size boolean values.
        """
        import math

        max_ele = max(arr)

        vis = [False] * (max_ele + 1)

        for ele in arr:
            vis[ele] = True

        for a in range(1, max_ele + 1):

            if not vis[a]:
                continue

            for b in range(1, max_ele + 1):

                if not vis[b]:
                    continue

                    c = int(math.sqrt(a * a + b * b))

                    if c * c != (a * a + b * b) or c > max_ele:
                        continue

                    if vis[c]:
                    return True

        return False


if __name__ == "__main__":
    arrs = [
        [],
    ]
    ans = Solution()
    print("******Brute Force******")
    for arr in arrs:
        print(ans.brute_force(arr))
    print("******Expected******")
    for arr in arrs:
        print(ans.expected_solution(arr))
