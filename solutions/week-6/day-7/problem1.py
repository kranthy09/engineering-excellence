"""
Remove Duplicates from sorted array
"""


class Solution:

    def brute_force(self, arr):
        pass

    def expected_approach(self, arr):
        """
        TC:
        SC:
        """
        # responsible for telling the position of unique element
        unique_pos = 1
        # responsible for fetching unique elements
        current_ele = 1
        hmap = {arr[0]: 1}
        while current_ele < len(arr):
            if hmap.get(arr[current_ele]):
                current_ele += 1
            else:
                arr[unique_pos] = arr[current_ele]
                hmap[arr[current_ele]] = 1
                unique_pos += 1
                current_ele += 1
        return arr[:unique_pos]


if __name__ == "__main__":
    arrs = [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
            [1, 2, 2, 2, 3, 3, 4, 4, 4, 9, 9, 10],
            [2, 2, 2, 2]
            ]
    ans = Solution()
    for arr in arrs:
        print(ans.expected_approach(arr))
