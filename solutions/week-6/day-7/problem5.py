"""
Longest substring with unique characters
"""


class Solution:

    def brute_force(self, *args, **kwargs):
        pass

    def expected_approach(self, *args, **kwargs):
        """

        TC:
        SC:
        """
        s = args[0]
        left = 0
        right = 0
        visited = {}
        maxx = 0
        while right < len(s):
            # print(visited)
            if visited.get(s[right]):
                maxx = max(maxx, right - left)
                # print(maxx)
                # print()
                while visited.get(s[right]):
                    visited[s[left]] -= 1
                    left += 1
            else:
                visited[s[right]] = 1
                right += 1
        return maxx


if __name__ == "__main__":
    strings = [
        "geeksforgeeks",
        "nmotrortsqtpun"
    ]
    ans = Solution()
    for s in strings:
        print(ans.expected_approach(s))
