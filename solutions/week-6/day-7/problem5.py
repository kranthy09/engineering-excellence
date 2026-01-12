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
        visited = {s[left]: 1}
        maxx = 0
        while right < len(s):
            if visited.get(s[right]):
                maxx = max(maxx, right - left)
                while left <= right:
                    if s[left] == s[right]:
                        visited = {s[left]: 1}
                        left += 1
                        right += 1
                        break
                    left += 1
            else:
                visited[s[right]] = 1
                right += 1
        return maxx


if __name__ == "__main__":
    string = "geeksforgeeks"
    ans = Solution()
    print(ans.expected_approach(string))
