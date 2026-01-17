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

        TC:O(n*m)
        AS:O(n)

        # TODO:
        # Create a map of {string, [list of indices]} and use them
        # to create the output. AS should be optimsed from O(nm) to
        # O(n)
        """
        arr = args[0]
        n = len(arr)
        hmap = {}
        for i in range(n):
            key = self.get_hash_key(arr[i])
            if hmap.get(key):
                hmap[key].append(arr[i])
            else:
                hmap[key] = [arr[i]]
        return [val for val in hmap.values()]

    def get_hash_key(self, subs):
        """
        Get hash for a string
        """
        repre = [0] * 26
        for i in range(len(subs)):
            repre[ord(subs[i]) - ord("a")] += 1
        key = ""
        for i in range(26):
            key += str(repre[i]) + "#"  # unique by delimiter
        return key

    def optimised_expected_approach(self, *args, **kwargs):
        """
        Continuing with expected approach, instead of storing list of
        strings, store their indices, will reduce AS from O(nm) to O(n)

        TC:
        AS:
        """
        arr = args[0]
        n = len(arr)
        hmap = {}
        for i in range(n):
            key = self.get_hash_key(arr[i])
            if hmap.get(key):
                hmap[key].append(i)
            else:
                hmap[key] = [i]
        res = []
        for indices in hmap.values():
            res.append([arr[i] for i in indices])

        return res


if __name__ == "__main__":
    arr = ["act", "god", "cat", "dog", "tac"]
    ans = Solution()

    print(ans.brute_force(arr))
    print(ans.expected_solution(arr))
