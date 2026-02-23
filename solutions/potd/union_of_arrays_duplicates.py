"""
Union Of Arrays Duplicates (Easy)
@topic: potd
@difficulty: easy
@tags: hash, arrays

You are given two arrays a[] and b[], return the Union of
 both the arrays in any order.

The Union of two arrays is a collection of all distinct
elements present in either of the arrays. If an element
appears more than once in one or both arrays, it should
be included only once in the result.

i/o: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
o/p: [1, 2, 3]


Approaches:
1. Expected: Hmap to store repeated and unique elements.
"""


class Solution:

    def find_union(self, a, b):
        """
        TC: O(n+m)
        AS: O(n+m), for maintaining hashmap.
        """

        na = len(a)
        nb = len(b)
        # hashmap to track elements.
        hmap = {}
        # output space.
        res = []
        for i in range(na):
            # increment count for repeated elements
            if hmap.get(a[i]):
                hmap[a[i]] += 1
            else:
                hmap[a[i]] = 1
                # element is new, add to result
                res.append(a[i])
        for j in range(nb):
            # just check the unique elements in "b".
            if not hmap.get(b[j]):
                hmap[b[j]] = 1
                # store to contribute union
                res.append(b[j])
        return res


if __name__ == "__main__":
    arrs = [
        [[1, 2, 3], [4, 5, 6]],  # [1, 2, 3, 4, 5, 6]
        [[1, 2, 1, 1, 2], [2, 2, 1, 2, 1]],  # [1, 2]
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.find_union(arr[0], arr[1]))
