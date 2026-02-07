"""
Longest substring with unique characters
"""


class Solution:

    def brute_force(self, *args, **kwargs):
        pass

    def expected_approach(self, *args, **kwargs):
        """
        Two pointers i, j at start of the arr, j traverse through elements
        in arr, i represent the starting of the subarray, maintain hashmap
        for characters seen while traversing, if the character(arr[j])
        already exists, shrint i, to eleminate the repetion found.

        Capture the substring length.

        TC: O(n)
        SC: O(1)
        """
        arr = args[0]
        n = len(arr)
        isPresent = [False] * 26
        i = 0
        j = 0
        result = 0
        while j < n:
            if not isPresent[ord(arr[j]) - ord("a")]:
                isPresent[ord(arr[j]) - ord("a")] = True
                result = max(result, j - i + 1)
            else:
                while s[i] != s[j]:
                    isPresent[ord(arr[i]) - ord("a")] = False
                    i += 1
                i += 1
            j += 1
        return result


if __name__ == "__main__":
    strings = [
        "geeksforgeeks",
        "nmotrortsqtpun"
    ]
    ans = Solution()
    for s in strings:
        print(ans.expected_approach(s))
