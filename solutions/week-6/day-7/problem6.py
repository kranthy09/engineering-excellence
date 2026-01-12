"""
Group anagrams together
"""


class Solution:
    def brute_force(self, *args, **kwargs):
        """
        For each string in array, compare with all strings, if they are equal
        group them. Comparision involves counting number of characters in both
        strings.

        TC: O(len(arr)*len(arr)*len(maxx)*)
        """
        pass

    def expected_solution(self, *args, **kwargs):
        """
        Convert strings to similar representations
        and create a hashmap with converted string as key
        to track the indexes to group

        TC:O(n*maxx)
        SC:O(unique(n))
        """

        arr = args[0]
        hmap = {}
        # convert
        for i in range(len(arr)):
            inte = 1
            for j in range(len(arr[i])):
                inte = inte << (ord(arr[i][j]) - ord('a'))
            print(inte, arr[i])
            if hmap.get(inte):
                hmap[inte].append(arr[i])
            else:
                hmap[inte] = [arr[i]]
        return [val for val in hmap.values()]


if __name__ == "__main__":
    arr = ["act", "god", "cat", "dog", "tac"]
    ans = Solution()

    print(ans.brute_force(arr))
    print(ans.expected_solution(arr))
