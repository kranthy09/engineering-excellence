"""
Meeting Rooms (Easy)
@topic: potd
@difficulty: easy
@tags: sorting, greedy, arrays

Given a 2D array arr[][], where arr[i][0] is the starting time
of ith meeting and arr[i][1] is the ending time of ith meeting,
the task is to check if it is possible for a person to attend all
the meetings such that he can attend only one meeting at a particular time.

Note: A person can attend a meeting if its starting time is
greater than or equal to the previous meeting's ending time.


i/o: [[1, 4], [10, 15], [7, 10]]
o/p: true



Approaches:
1. Expected: Sort and check the end of meeting with start of next.
"""


class Solution:
    def can_attend(self, arr):
        # Code Here
        n = len(arr)

        # sort the meeting, as the time is required to attend the meeting
        # not the order
        arr = sorted(arr, key=lambda arr: arr[0])

        # for each meeting, check with next meeting timings
        for i in range(n-1):

            # first meeting end time
            end_ = arr[i][1]

            # next meeting start time

            start_ = arr[i+1][0]

            # if they collide
            if end_ > start_:
                return False
        return True


if __name__ == "__main__":
    arrs = [
        [[1, 4], [10, 15], [7, 10]],
        [[2, 4], [9, 12], [6, 10]],
    ]
    ans = Solution()
    print("******can_attend******")
    for arr in arrs:
        print(ans.can_attend(arr))
