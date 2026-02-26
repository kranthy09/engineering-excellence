"""
Isomorphic Strings (Easy)
@topic: potd
@difficulty: easy
@tags: strings, hash

Given two strings s1 and s2 consisting of only lowercase
English letters and of equal length, check if these two
strings are isomorphic to each other.
If the characters in s1 can be changed to get s2, then two
strings, s1 and s2 are isomorphic. A character must be completely
swapped out for another character while maintaining the order of
the characters. A character may map to itself, but no two characters
may map to the same character.

i/o: s1 = "aab", s2 = "xxy"
o/p: true


Approaches:
1. Expected: Store characters in 26 length array map, O(n)
"""


class Solution:

    def are_isomorphic(self, s1, s2):
        """
        TC: O(n)
        AS: O(1), extra space by arrays will be of 26 alphabets, constant.
        """

        n = len(s1)
        # to store visited elements of s2
        marked = [False] * 26
        # to store elements of s1
        map_ = [-1] * 26

        for i in range(n):
            # reduce between 0 to 25
            u = ord(s1[i]) - ord('a')
            v = ord(s2[i]) - ord('a')

            # new character
            if map_[u] == -1:

                # checks s2 is already visited by previous element in s1.
                if marked[v]:
                    return False
                # relate the s1, s2 elements
                map_[u] = v
                # mark the s2 element as visited, True.
                marked[v] = True
            else:
                # if the created relation doesnot hold for new chars
                if map_[u] != v:
                    return False
        return True


if __name__ == "__main__":
    arrs = [
        ["aab", "xxy"],  # True
        ["aab", "xuz"],  # False
        ["abc", "xxy"]  # False
    ]
    ans = Solution()
    for arr in arrs:
        print(ans.are_isomorphic(arr[0], arr[1]))
